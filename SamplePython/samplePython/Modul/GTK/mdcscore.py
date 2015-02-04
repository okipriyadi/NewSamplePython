'''
Created on Jul 22, 2014

@author: andri
'''

import os
import sys
import tempfile
import datetime
import logging
import threading
import shutil
import cgi
import time
import distutils.dir_util
import glob

#TODO : change to local library/class for handling FDCS thingy
# from repository.local_repository import LocalRepository
# from repository.sftp_repository import SFTPRepository
# from manager.fdcu_manager import FDCUManager
# from core.errors import *


if sys.platform == 'win32':
	import win32api
	import win32file

# add libs path to sync_manager path
sys.path.append(
os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '../..', 'libs'))
# 
# from core import config
from libs import config
from libs import common
from libs.fdcsapi import FDCSAPI
from libs import listeners
from libs import hash
from libs.storage_watcher import StorageWatcher 
from libs.bfcipher import BFCipher 
from mdcsdb import MDCSDB

class MDCSCore(object):
	'''
	Core MDCS Helper
	'''
	#mdcscore constant
	PATH_MDSC_DATABASE					= 100
	PATH_REPO_ROOT						= 200
	PATH_REPO_ACRL						= 201
	PATH_REPO_ACRLSTAT					= 202
	PATH_REPO_DATA						= 203
	PATH_REPO_MANIFEST					= 204
	PATH_REPO_UPLOAD					= 205
	PARTIALLY_DOWNLOADED_EXT			= '__part__'
	MIN_BUFFER_SIZE						= 1024
	BUFFER_SIZE							= 16 * 1024
		
	# shared properties for MDCSUI
	#data
	localrepo_path = ''
	aircraft_data = []
	acrl_data = []
	fleet_info = []
	fdcu_manifest = {}
	data_files = []
	number_acrl_files = 0 
	total_acrl_filesize = 0
	
	current_acrlname = ''
	current_fleetname = ''
	current_targetfolder = ''
	current_srcfolder = ''
	root_target_path = ''
	
	removable_device_list = []
	target_removable = ''
	target_removable_list = [] #to store used device to copy, to keep list copy information
	added_files = []
	deleted_files = []
	
	#progress status
	copy_status = ''
	status_text = ''
	listener = None
	overall_progress = -1
	overall_progress_text = ''
	overall_size_progress = 0
	overall_total_size = 0
	overall_file_progress = 0
	overall_total_file = 0
	close = False #for stopping progress
	is_processing = False
	is_updating_aircraft_list = False
	download_done = False
	resume = False
	is_run = False
	is_reconnectiong = False
	retry = 0
	is_processing_download = False
	is_processing_upload = False
	is_processing_housekeeping = False
	terminate = False
	starting_process = None
	config = None
	
	def init_config(self):
		self.conf_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'conf')
		self.config = config.get_config(relative_path=self.conf_dir,config_filename='mdcs.ini')
	
	def reinit_config(self):
		self.init_config()
		
	def __init__(self,conf = None):
		
		if conf is None:
			self.init_config()
# 			self.conf_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'conf')
# 			self.config = config.get_config(relative_path=self.conf_dir,config_filename='mdcs.ini')
		else:
			self.config = conf 
# 		self.config = config.get_config()
		self.localrepo_path = self.config.get('general','local_repo')

		#create local repo structure if not exist
		self.createRepo(self.localrepo_path)
		self.mdcs_repo = MDCSRepositoryHelper()

		self.temp_local_path = os.path.join(tempfile.gettempdir(), "mdcs")
		self.mDB = MDCSDB(conf = self.config)
		self.mEvent = None
		
		self.callback = None
		self.thread_isolator = MDCSThreadIsolator()
		self.thread_isolator.core = self
		self.thread_isolator.start()
		
		#check mounted removable media on system 
		self.removable_device_list = self.mdcs_repo.get_removables()
		print self.removable_device_list
		
		#run storage watcher to update removable list
		storagewatcher = StorageWatcher(self.updateRemovableList)
		storagewatcher.run()	
		
		self.listener = MDCSTransferListener(self)
		pass

	def set_mdcs_event(self, mEvent): 
		self.mEvent = mEvent
	
	def set_mdcs_ui(self, mUI):
		self.mUI = mUI

	def set_thread_callback(self, fun):
		self.callback = fun
	
	def run_in_thread(self, fun, *args):
		"""
		Run a function in isolated thread
		"""
		self.thread_isolator.set_target(fun, *args)
		#t.join()
	
	def terminate_process(self):
		"""
		Try to terminate current process, close all resources and database
		"""
		if self.is_reconnectiong and self.callback != None:
			self.is_reconnectiong = False
			self.callback()
			self.callback = None
			self.status_text = ""
			
		if self.is_processing:
			self.terminate = True
			self.overall_progress = -1
			self.overall_progress_text = ''
			self.is_reconnectiong = False
			self.status_text = "Terminating..."
			try:
				self.selected_source.close_repo()
			except:
				pass
			try:
				self.selected_target.close_repo()
			except:
				pass
			self.is_processing = False
			self.is_processing_download = False
			self.is_processing_upload = False
			self.is_processing_housekeeping = False

	def timestamp(self):
		return time.strftime('%Y/%m/%d %H:%M:%S')

	def createRepo(self,path):
		#root
		if not os.path.exists(path):
			os.makedirs(path)
		#db
		if not os.path.exists(os.path.join(path,'db')):
			os.makedirs(os.path.join(path,'db'))
		#acrl
		if not os.path.exists(os.path.join(path,'acrl')):
			os.makedirs(os.path.join(path,'acrl'))
		#acrldatastat-uploaded
		if not os.path.exists(os.path.join(path,'acrldatastat','uploaded')):
			os.makedirs(os.path.join(path,'acrldatastat','uploaded'))
		#data
		if not os.path.exists(os.path.join(path,'data')):
			os.makedirs(os.path.join(path,'data'))
		#manifest
		if not os.path.exists(os.path.join(path,'manifest')):
			os.makedirs(os.path.join(path,'manifest'))
		#upload
		if os.path.exists(os.path.join(path,'upload')):
			os.makedirs(os.path.join(path,'upload'))
	
	def get_path(self, path_code):
		if path_code == self.PATH_REPO_ACRL:
			return os.path.join(self.localrepo_path,'acrl')
		elif path_code == self.PATH_REPO_ACRLSTAT:
			return os.path.join(self.localrepo_path,'acrldatastat','uploaded')
		elif path_code == self.PATH_REPO_DATA:
			return os.path.join(self.localrepo_path,'data')
		elif path_code == self.PATH_REPO_MANIFEST:
			return os.path.join(self.localrepo_path,'manifest')
		elif path_code == self.PATH_REPO_UPLOAD:
			return os.path.join(self.localrepo_path,'upload')
		else:
			return ""
	pass
	
	def refreshFDCUManifest(self):
		fdcs_api = FDCSAPI(conf = self.config)
		self.fdcu_manifest = fdcs_api.getFDCUManifest()
		
		if self.fdcu_manifest is None: 
			error = 'Failed to get FDCU Manifest from FDCS, check connection'
			print(error)
			logging.info('Failed to get FDCU Manifest from FDCS, check connection')
			return error
		
		for key, value in self.fdcu_manifest.iteritems():
			print key,value
			logging.info('key : %s' % key)
			logging.info('value : %s' % value)

		#get aircraf list
		self.aircraft_data = self.fdcu_manifest['aircrafts']
		#get datagroup/acrl list
		self.acrl_data = self.fdcu_manifest['acrls']
		#get fleet info list
		self.fleet_info = self.fdcu_manifest['fleets']

		#get fdcu info from DB
		fdcu_info_db = self.mDB.getFDCU(self.config.get('fdcu', 'name'))
		
		if fdcu_info_db is None:		
				#insert new FDCU
			fdcu_id = self.mDB.insertFDCU(self.fdcu_manifest)	

			for fleet in self.fleet_info:
	
				#insert fleet list
				fleet_id = self.mDB.insertFleet(fdcu_id,fleet)
				#insert aircraft list based on fleet aircraft list
				#loop aircraft
				fleet_aircrafts = fleet['aircrafts']
				for fleet_aircraft in fleet_aircrafts:
					for aircraft in self.aircraft_data:
						#if fleet tn = aircraft tn insert to db
						if fleet_aircraft == aircraft['tail_number'] :
							self.mDB.insertAircraft(fleet_id,aircraft)
							break
	
				#insert  datagroup list based on fleet group list
				#loop acrl
				fleet_groups = fleet['groups']
				for fleet_group in fleet_groups:
					for acrl in self.acrl_data:
						#if fleet acrlname = aircraft acrlname insert to db
						datagroup, ext = acrl['group'].rsplit('.',1)
						name, profile, version = datagroup.rsplit('_',2)
						
						if fleet_group['group'] == name and fleet_group['category'] == acrl['category']:
							self.mDB.insertACRL(fleet_id,acrl)
							break
			
		else:
			#update data
			self.mDB.updateFDCU(self.fdcu_manifest)	
			fdcu_id = fdcu_info_db.id_
			#update fleet 
			self.mDB.updateFleet(fdcu_id,self.fleet_info)	

			for fleet in self.fleet_info:
				#update aircraft
				self.mDB.updateAircraft(fleet,self.aircraft_data)	
				#update datagroup
				self.mDB.updateACRL(fleet,self.acrl_data)	
			
	
	def updateRemovableListInfo(self):
		self.removable_device_list = []
		self.removable_device_list = self.mdcs_repo.get_removables()
		
	def updateRemovableList(self,device):

		if device.action == 'add':
			#get device info
			print(self.timestamp()+" | New storage partition was added : {0.device_node}, {0.device_type}".format(device))
			#check and get mount point
			time.sleep(2) #delay 2 sec, to wait device mounted
			mountsFile = open('/proc/mounts')
			lines2 = mountsFile.readlines()
			for line2 in lines2:
				words2 = [x.strip() for x in line2.split()]
				if words2[0] == device.device_node:
					drname = words2[1]
					label = drname
					available_size = common.get_available_space_size(drname)
					total_size = common.get_total_space_size(drname)
					label = "{0} - ({1} free of {2})".format(label, common.sizeof_fmt(available_size), common.sizeof_fmt(total_size))
					

			isFound = False
			index = 0
			for removable in self.removable_device_list:
				if removable[0] == drname:
					isFound = True
					del self.removable_device_list[index]
					break
				index+=1
			
# 			if not isFound:
			self.removable_device_list.append([drname,label,device.device_node])

		if device.action == 'remove':
			print self.timestamp()+" | Storage partition was removed : {0.device_node}, {0.device_type}".format(device)
			index = 0
			for removable in self.removable_device_list:
				if removable[2] == device.device_node:
					del self.removable_device_list[index]
					break
				index+=1

		self.mEvent.build_removable_device_list()		
		pass
		
	def findTargetRootPath(self,acrlitems):
		print 'findTargetRootPath:'
		#create new dir
		root_path = '/'
		if acrlitems is not None and len(acrlitems) > 0:
			if acrlitems['datagroup_files'] is not None and len(acrlitems['datagroup_files']) > 0:
				root_path = acrlitems['datagroup_files'][0]['target']
				for datafile in acrlitems['datagroup_files']:
					path = datafile['target'].split('/')
					if len(path) == 2 and path[1] == '': #path is /
						root_path = datafile['target']
						break
					elif len(path) < len(root_path.split('/')): #path shorter then rootpath
						root_path = datafile['target']

		print 'root path:', root_path
		return root_path
		
	def createTempTargetPathFolder(self,fleet_name,acrl_name,acrlitems):
		
		#create tree of target path
		root_path = '.temp'+os.sep+'%s' %fleet_name +os.sep+'%s' %acrl_name
		#clear all path 
		try:
			shutil.rmtree(root_path)
		except :
			pass
		
		#create new dir
		for datafile in acrlitems['datagroup_files']:
			added_path = root_path + datafile['target']
			if not os.path.exists(added_path):
				os.makedirs(added_path)
		
		pass
			
	def getAcrlDBList(self,fleet_name,group_name = None):
			return self.mDB.getACRLList(fleet_name,group_name = group_name)

	def getFleetDataFiles(self,fleet_name,group_name = None):
			#get MEDIA acrlname based on fleet name
			print 'getFleetDataFiles:'
			acrls = self.mDB.getACRLList(fleet_name,group_name = group_name)
			
			self.number_acrl_files = 0 
			self.total_acrl_filesize = 0
			#get datafiles from fdcs
			if len(acrls) > 0:
				total_filenumber = 0
				total_filesize = 0
				for acrl in acrls:
					fdcs_api = FDCSAPI(conf = self.config)
					acrlitems = fdcs_api.getMediaList(acrl.group_name_,fleet_name)
					
					#todo add update or delete datafiles
					#insert to database
					print 'acrlitems = '
					print acrlitems
					
					if acrlitems is not None:
						#get root of target_path
						self.root_target_path = self.findTargetRootPath(acrlitems)
						#create temp folder structure from target path
						self.createTempTargetPathFolder(fleet_name,acrl.name_,acrlitems)
						self.mDB.deleteDataFile(fleet_id=acrl.fleet_id_, group_id=acrl.id_)
						print 'insert new data file'
						for acrlitem in acrlitems['datagroup_files']:
							#check if file exist in local source dir
							fileid, filename = acrlitem['file'].split('_',1)
							total_filesize = total_filesize + float(acrlitem['size'])
							
							src_path = self.searchSourcePath(self.config.get('general','source_dir'),filename,acrlitem['sum']) 
							
							self.mDB.insertDataFile(acrl.id_,acrlitem,acrl.fleet_id_,src_path)
						#endfor
# 						self.current_acrlname = acrl.name_
						total_filenumber = total_filenumber + len(acrlitems['datagroup_files']) 
						print 'total file number :',total_filenumber
				#endfor	
				self.number_acrl_files = total_filenumber
				self.total_acrl_filesize = total_filesize
				#get datafile from database
				#todo : /media should set on setting page/configuration page
# 				self.data_files = self.mDB.getDataFile(acrls[0].id_,acrl.fleet_id_,'/media')
# 			return self.data_files

	def getDataFile(self,fleet_name, target_path):
		self.data_files = self.mDB.getDataFileFromName(self.current_acrlname,fleet_name,target_path)
		return self.data_files
		
		
	def addDataFile(self,group_name, target_path, file_name, file_size, file_sha, eff_start_ts, eff_end_ts):
		
		#insert to fdcs
		fdcs_api = FDCSAPI(conf = self.config)
		file_stat = fdcs_api.addDataFile(group_name, target_path, file_name, file_size, file_sha, eff_start_ts, eff_end_ts)
		
		logging.info('add file response :')
		logging.info(file_stat)
		print 'add file response :'
		print file_stat
		#insert to local db
# 		self.mDB.insertDataFile(group_id, acrl_item, fleet_id)
		return file_stat

	def addDataFiles(self,added_files):
		#added_files is list of dict of added file
		#insert to fdcs
		fdcs_api = FDCSAPI(conf = self.config)
		add_files_stat = fdcs_api.addDataFiles(added_files)
		
		logging.info('add file response :')
		logging.info(add_files_stat)
		print 'add files response :'
		print add_files_stat
		#insert to local db
# 		self.mDB.insertDataFile(group_id, acrl_item, fleet_id)
		
		return add_files_stat
		
	def addFolderFiles(self, current_folder, foldername, folderpath):
		#walk to the deep of folderpath :)
		rootfolder, temp = folderpath.split(foldername) 
		for root,folders,files in os.walk(folderpath):

			#get active dir
			tmp, active_dir = root.split(rootfolder) 
			
			target_path = current_folder+os.sep+active_dir
			#cleanup // if exist, replace to /
			target_path = target_path.replace('//','/')

			for folder in folders:
# 				new_dir = os.path.join('.temp',self.current_fleetname,self.current_acrlname,target_path,folder)
				new_dir = '.temp' +os.sep+self.current_fleetname+os.sep+self.current_acrlname+os.sep+target_path+os.sep+folder
				if not os.path.exists(new_dir):
					os.makedirs(new_dir)
			
			for fl in files:
# 				fl_path = os.path.join(root,fl)
				fl_path = root+os.sep+fl
				file_status_list = self.addDataFile(self.current_acrlname,
												target_path,
												fl, 
												os.path.getsize(fl_path),
												hash.sha1sum(fl_path), 
												'2014-10-06',
												'2015-10-06')
				print file_status_list
		
		
	def deleteFolderFiles(self,current_folder, folder_name):
		#TODO : delete all files in folder and subfolders from FDCS recursively
		#recursif process to delete all folder content
		#walk to the deep of folderpath :)
		temp_folder = '.temp' +os.sep+self.current_fleetname+os.sep+self.current_acrlname+current_folder+os.sep+folder_name
		rootfolder = current_folder + os.sep + folder_name
		print 'temp_folder = ', temp_folder
		print 'rootfolder = ', rootfolder

		for root,folders,files in os.walk(temp_folder,topdown=False): #bottom up walk
# 			target_path = os.path.join(target_path,foldername)
			tmp, active_dir = root.split(temp_folder) 
			print 'active_dir = ', active_dir

			target_path = rootfolder+active_dir
			#cleanup // if exist, replace to /
			target_path = target_path.replace('//','/')
			print 'target_path = ', target_path

			db_list_files = self.getDataFile(self.current_fleetname, target_path)
			
			for fl in db_list_files:
				resp = self.deleteDataFile(self.current_acrlname, fl.filename_)
				if resp == 'OK':
					print 'file %s, deleted' %fl.filename_
				else :
					print 'file %s, delete failed' %fl.filename_
			#delete folder tree structure recursively
			
# 			shutil.rmtree(temp_folder+os.sep+active_dir)

		pass

	def deleteDataFile(self,group_name, file_name):
		
		#insert to fdcs
		fdcs_api = FDCSAPI(conf = self.config)
		resp = fdcs_api.cancelDataFile(group_name, file_name)
		
		print 'resp_delete = %s' %resp
		#insert to local db
# 		self.mDB.insertDataFile(group_id, acrl_item, fleet_id)
		
		return resp

	def updateMDCSLocalRepo(self):
		print 'updateMDCSLocalRepo:'
		#get AC Manifest file from FDCS
		aircraft_list_db = self.mDB.getAircraftListbyFleetName(self.current_fleetname)
		for aircraft in aircraft_list_db:
			self.getACManifest(aircraft.tail_number_,aircraft.airline_)
# 			print ac_manifest

		acrl_list_db = self.mDB.getACRLList(self.current_fleetname)
		for acrl in acrl_list_db:
			acrl_name,ext = acrl.group_name_.split('.')
			self.getACRLDB(acrl_name,aircraft_list_db)
	
	def getACManifest(self,tail_number,airline):
		#put ac manifest to local repo
		print 'getACManifest:'
		#get ac manifest to fdcs
		fdcs_api = FDCSAPI(conf = self.config)
		res = fdcs_api.getAircraftManifestFile(tail_number)

		if res is not None:
			try:
				_, params = cgi.parse_header(res.headers.get('Content-Disposition', ''))
				filename_cgi = params['filename']	
				print 'ac manifest filename = ',filename_cgi		
				
				tn, tempsum = filename_cgi.rsplit('-',1)
				checksum, ext = tempsum.split('.')

				#create ac mnanifest file
				filename = tn+'.'+ext
				fpathname = self.get_path(self.PATH_REPO_MANIFEST)+os.sep+filename
				f = open(fpathname, 'wb')
				block_sz = 8192
				while True:
					buff = res.read(block_sz)
					if not buff:
						break
				
					f.write(buff)
				
				f.close()
				
				#create ac manifest sum file 
				fsumname = fpathname+'.sum'
				fsum = open(fsumname, 'wb')
				fsum.write(checksum)
				fsum.close
				fsum.flush()
				
				print 'ac manifest sum = ',checksum
				print 'ac manifest file hash = ',hash.sha1sum(fpathname)
				
# 				#put manifest to airline folder
# 				airline_path = os.path.join(self.get_path(self.PATH_REPO_MANIFEST),airline)
# 				
# 				if not os.path.exists(airline_path):
# 					os.makedirs(airline_path)
# 
# 				fairline_pathname = airline_path+os.sep+filename
# 				fairline_pathname_sum = airline_path+os.sep+filename+'.sum'
# 				
# 				shutil.copyfile(fpathname, fairline_pathname)
# 				print 'aircraft manifest file hash on airline folder = ',hash.sha1sum(fairline_pathname)
# 				shutil.copyfile(fsumname, fairline_pathname_sum)
				

			except Exception as ex:
				print 'getManifest error : ', ex
				logging.error('getManifest Error : %s' %ex)

	def getACRLDB(self,acrl_name,aircraft_list):
		#put acrldb to local repo
		print 'getACRLDB:'

		#get acrldb  from fdcs
		fdcs_api = FDCSAPI(conf = self.config)
		res = fdcs_api.getACRLDBFile(acrl_name)

		if res is not None:
			try:
				_, params = cgi.parse_header(res.headers.get('Content-Disposition', ''))
				filename = params['filename']	
				print 'acrl filename = ',filename		
				
				acrlname, tempsum = filename.rsplit('-',1)
				checksum, ext = tempsum.split('.')
				
				#delete all old acrl version
				#get acrlname only without csci and version
				name, csci, version = acrlname.rsplit('_')
				for del_file in glob.glob(self.get_path(self.PATH_REPO_ACRL)+os.sep+name+'*'):
					os.remove(del_file)

				#create acrl dbfile
				fname = self.get_path(self.PATH_REPO_ACRL)+os.sep+acrlname+'.'+ext
				
				#delete old acrl 
				
				
				f = open(fname, 'wb')
				block_sz = 8192
				while True:
					buff = res.read(block_sz)
					if not buff:
						break
				
					f.write(buff)
				
				f.close()
				
				print 'acrl sum = ',checksum
				print 'acrl file hash = ',hash.sha1sum(fname)
# 				#copy file and add tail_number to the file
# 				for aircraft in aircraft_list:
# 					
# 					acrlairline_path = os.path.join(self.get_path(self.PATH_REPO_ACRL),aircraft.airline_)
# 					
# 					if not os.path.exists(acrlairline_path):
# 						os.makedirs(acrlairline_path)
# 
# 					facrldbname = acrlairline_path+os.sep+aircraft.tail_number_+'_'+acrlname+'.'+ext
# 					
# 					shutil.copyfile(fname, facrldbname)
# 					print 'aircraft acrl file hash = ',hash.sha1sum(facrldbname)
# 				
			except Exception as ex:
				print 'getACRLDB error : ', ex
				logging.error('getACRLDB Error : %s' %ex)
		pass

	def searchSourcePath(self,src_dir,filename,checksum):
		print 'searchSourcePath for %s :' %filename
		filepath = None
		found = False
		#walk src dir
# 		print 'search Source Path, src dir = ',src_dir
		for root,subdirs,files in os.walk(src_dir):

			files = [f for f in files if not f[0] == '.']
			for fl in files:
				if fl == filename:
					fl_fullpath = root+os.sep+fl
					if hash.sha1sum(fl_fullpath) == checksum:
						found = True
						filepath = fl_fullpath	
# 						print ('---\nfile = ' + fl)

			if found:
				break
		
		print 'filepath:',filepath
		return filepath


	def targetRemovableExist(self,target):
		#add new target to list
		isExist = False
		for target_removable in self.target_removable_list:
			if target == target_removable:
				isExist = True
				break
		
		return isExist
						
	# copy the file
	def copy_(self, source, target, listener):
		
		done = False
		isSuccess = False
		
		try:
			fsource = open(source, "rb")
			ftarget = open("{0}{1}".format(target, self.PARTIALLY_DOWNLOADED_EXT), "wb")
			
			# total size of files
			size = os.stat(source).st_size
			self.overall_total_size = size
			
			if size / self.BUFFER_SIZE == 0:
				buffer_size = self.MIN_BUFFER_SIZE
			else:
				buffer_size = self.BUFFER_SIZE
			
			if(listener is not None):
				listener.start(source, target, size)
	
			block_pos = 0
			while True and not self.close:
				
				cur_block = fsource.read(buffer_size)
				#check if mode = encrypted
				#do encryption think, write to file
	
				if cur_block:
					block_pos += len(cur_block)
					ftarget.write(cur_block)
					if(listener is not None):
						listener.update(block_pos)
				else:
					ftarget.flush()
					os.fsync(ftarget.fileno())
					done = True
					break
	
			if(listener is not None):
				listener.end()
		finally:
			try:
				fsource.close()
			except:
				pass
			try:
				ftarget.close()
			except:
				pass
			
			if(listener is not None):
				listener.end()

			if done:
				# check size
				if os.stat(ftarget.name).st_size != size:
					try:
						os.remove(ftarget.name)
					except:
						pass
					raise Exception("Size doesn't match")
				
				try:
					os.remove(target)
				except:
					pass
				
				os.rename(ftarget.name, target)
				
				isSuccess = True
				
		# force to remove .part file
		part_file = "{0}{1}".format(target, self.PARTIALLY_DOWNLOADED_EXT)
		if os.path.exists(part_file):
			try:
				os.remove(part_file)
			except Exception as e:
				pass
			
			
		return isSuccess
	# end transfer

	def copyMetaData(self):
		try:
			if not os.path.isfile(self.target_removable+os.sep+'USBFDCU'):
				open(self.target_removable+os.sep+'USBFDCU', 'a').close()
				
			#create repo folder structure 
	# 		self.createRepo(self.target_removable)

			#copy acrl, manifest, acrldatastat from local repo folder to removable disc recursively
			distutils.dir_util.copy_tree(self.localrepo_path, self.target_removable)
			print 'Metadata copied to removable disk'
			return True
		
		except Exception as ex:
			print 'copy MetaData failed : ', ex
			return False
		
	def processCopyFile(self,data_file):
		print 'processCopyFile :'

		ffiles = None
		try:
			
			if data_file.sourcepath_ is None:
				print 'source path is  None for %s file, ' %data_file.filename_
				return
				
			filename_enclist = os.path.join (self.target_removable,self.current_acrlname+'.enc')
# 			encfile_checksum = ''
			ffiles = open(filename_enclist, 'a+')
			
			self.overall_file_progress += 1
			
			
			file_id, filename = data_file.filename_.split('_',1)
			print 'filename = ', filename
			data_path = os.path.join(self.target_removable,'data')
			print 'data_path = ',data_path
			target_datafile = data_path+os.sep+filename
			print 'target_datafile = ', target_datafile
			print 'file checksum = ', data_file.checksum_

			#double check
			#check if file exist and same checksum, skip
			if not os.path.isfile(target_datafile): #and hash.sha1sum(target_datafile) != data_file.checksum_:

				if data_file.filesize_ <= common.get_available_space_size(self.target_removable):
					#encrypt file
					enc_filename = data_file.sourcepath_+'_enc'
					key = data_file.checksum_ #An arbitrarily long key
					bfc = BFCipher(key)
	
					#encrypt file shall return true/false if the encrypting process successful or failed 
					self.copy_status = 'Encrypting file %s' %filename
					time.sleep(0.5)
					print 'Encrypting file'
					bfc.encryptfile(data_file.sourcepath_,enc_filename)
					encfile_checksum = hash.sha1sum(enc_filename)
					print 'Encrypted file checksum :', encfile_checksum
	
					#check if encrypted file created successfully
					if os.path.exists(enc_filename):
						
						print 'Copying file to target device'
						self.copy_status = 'Copying file %s' %filename
						if (self.copy_(enc_filename,target_datafile, listener=self.listener)):
						#check file check sum, if ok, keep the file, 
		#				if hash.sha1sum(target_datafile) != data_file.checksum_:
							if hash.sha1sum(target_datafile) != encfile_checksum:
								print 'File checksum not valid, delete file'
								if os.path.exists(target_datafile):
									try:
										os.remove(target_datafile) 
									except Exception as ex: 
										print 'Remove temporary encrypted file failed : ', ex
	
							else :
								#write to target device list file
								ffiles.writelines('%s;%s\n' %(encfile_checksum,filename,))
								print 'copy file %s successful' % filename
								self.copy_status = 'copy file %s successful' % filename
	
						else :
							print 'copy file %s failed' % filename
							self.copy_status = 'copy file %s failed' % filename
	
						#remove temporary file
						try:
							os.remove(enc_filename)
						except Exception as ex: 
							print 'Remove temporary encrypted file failed : ', ex
							pass
					else:
						print 'Create encrypted file failed'
						self.copy_status = 'Create encrypted file failed'
				else:
					return -1 #not enough space
			else:
				ffiles.writelines('%s;%s\n' %(data_file.checksum_,filename,))
					
				print 'File %s already exist in usbfdcu' % filename
				self.copy_status = 'File %s already exist in usbfdcu' % filename
			ffiles.close()
		except Exception as ex:
			if not ffiles.close:
				ffiles.close()
				
			print 'Error when copying file :', ex	
			self.copy_status = 'Error when copying file : %s'% ex	
			
		

	def __copyToRemovable(self): #not used, moved to mdcsevent
		#copy meta data and data files to removable disk
		print self.localrepo_path
		print self.target_removable
		print self.current_fleetname
		print self.current_acrlname
		
		self.is_processing_download = True
		try:
			#check if USBFDCU file exist, create if not exist
			if self.target_removable == '':
				print 'target usb/sdcard disk not selected, please select'
				return
			
			#copy metadata
			self.copyMetaData()
			
			#copy datafiles from source 
			#get acrl data files
			list_data_file = self.getDataFile(self.current_fleetname,target_path=None)
# 			list_data_file = self.mDB.getDataFileFromName(self.current_acrlname,self.current_fleetname,target_path=None)		#get acrl data files
			#start copy to removable disk (basic function) 
			#list data file structure
			# item.id_ = row[0]
			# item.filename_ = row[1]
			# item.filesize_ = row[2]
			# item.targetpath_ = row[3]
			# item.checksum_ = row[4]
			# item.type_ = row[5]
			# item.group_id_ = row[6]
			# item.fleet_id_ = row[7]
			# item.sourcepath_ = row[8]
			
			self.overall_total_file = len(list_data_file)
			
			for data_file in list_data_file:
				#process copying files to removable disk
				self.processCopyFile(data_file)
		
		except Exception as e:
			print e

		
		self.is_processing_download = False
		self.overall_total_file = 0
		self.overall_file_progress = 0
		
		
	def getFolderSize(self,path):
		total_size = 0
		for dirpath, dirnames, filenames in os.walk(path):
			for f in filenames:
				fp = os.path.join(dirpath, f)
				total_size += os.path.getsize(fp)
		
		return total_size

class MDCSThreadIsolator(threading.Thread):
	"""
	MDCSCore thread isolator, to make sure called function is only running on a single thread
	and not using same resource at the same time
	"""
	core = None
	lock = threading.Lock()
	wait_lock = threading.Lock()
	stop = False
	_target = None
	_args = None
	
	def set_target(self, target, *args):
		self._target = target
		self._args = args
		
		self.wait_lock.release()

	def run(self):
		while not self.stop:
			if self._target is not None:
				self.lock.acquire()
				try:
					self._target(*self._args)
				except Exception as e:
					logging.error(str(e))
					self.core.status_text = str(e)
				self._target = None
				self.lock.release()
			self.wait_lock.acquire(True)
			
			
class MDCSTransferListener(listeners.TransferListener):
	"""
	Custom listener for generic file transfer
	"""
	def __init__(self, core):
		self.core = core
	
	def start(self, source, target, size):
		logging.info("Transferring {0} / {1} bytes".format(os.path.basename(source), size))
		self.size = size
		self.core.overall_size_progress = 0
		self.core.overall_progress = 0
		self.core.overall_progress_text = os.path.basename(target)

	def update(self, size):
		logging.debug("Transferred {0} bytes".format(size))
		progress = (size * 100) / self.size
		self.core.overall_progress = progress
		self.core.overall_size_progress = size

	def end(self):
		logging.debug("End transferring")
		self.core.overall_progress = -1
		self.core.overall_progress_text = ''
		self.core.overall_size_progress = 0
		self.overall_progress = 0
		#self.core.overall_progress_text = ''


class MDCSRepositoryHelper:
	"""
	Repository helper, mainly used by DDTUI
	"""
	(SFTP, FIXED, REMOVABLE, ANDROID) = (1, 2, 3, 4)
	
	def __init__(self):
		self.config = config.get_config()
	
	def get_repositories(self):
		pass

	def get_removables(self):
		"""
		Get available repositories, support common OS such as Windows and Linux
		"""
# 		fdcs = [self.config.get("ground", "hostname"), "FDCS", self.SFTP]
# 		fixed = []
		removeable = []
# 		android = []
		
		# perform Win32 storage lookups
		if sys.platform == 'win32':
			drivebits = win32api.GetLogicalDrives()
			for d in range(1, 26):
				try:
					mask = 1 << d
					if drivebits & mask:
						# here if the drive is at least there
						drname = '%c:\\' % chr(ord('A') + d)
						t = win32file.GetDriveType(drname)
						vi = win32api.GetVolumeInformation(drname)
						if t == win32file.DRIVE_REMOVABLE:
							label = self.get_label(drname, vi[0])
							#FIXME: add size to label
							repo = None
							try:
								pass
# 								repo = UsbRepository(mount_point=drname)
# 								repo.open_repo()
# 								available_size = repo.get_available_space_size(repository.PATH_GLOBAL_REPOSITORY_DATA)
# 								total_size = repo.get_total_space_size(repository.PATH_GLOBAL_REPOSITORY_DATA)
# 								label = "{0}\n({1} free of {2})".format(label, sizeof_fmt(available_size), sizeof_fmt(total_size))
							except Exception as e:
								logging.error(e)
							finally:
								try:
									repo.close_repo()
								except:
									pass

							removeable.append([drname, label])
				except:
					# skip
					pass

		# perform Linux devices lookups
		else:
			# find removables here
			partitionsFile = open("/proc/partitions")
			lines = partitionsFile.readlines()[2:]#Skips the header lines
			for line in lines:
				words = [x.strip() for x in line.split()]
				minorNumber = int(words[1])
				deviceName = words[3]
				if (minorNumber % 16) >= 0:
					path = "/sys/class/block/" + deviceName
					if os.path.islink(path):
						if os.path.realpath(path).find("/usb") > 0:
							dname = "/dev/%s" % deviceName
							mountsFile = open('/proc/mounts')
							lines2 = mountsFile.readlines()
							for line2 in lines2:
								words2 = [x.strip() for x in line2.split()]
								if words2[0] == dname:
									drname = words2[1]
									label = self.get_label(drname, os.path.basename(drname))
									#FIXME: add size to label
									repo = None
									try:
										pass
# 										repo = UsbRepository(mount_point=drname)
# 										repo.open_repo()
										available_size = common.get_available_space_size(drname)
										total_size = common.get_total_space_size(drname)
										label = "{0} - ({1} free of {2})".format(label, common.sizeof_fmt(available_size), common.sizeof_fmt(total_size))
									except Exception as e:
										logging.error(e)
									finally:
										try:
											repo.close_repo()
										except:
											pass

									removeable.append([drname, label, dname])

		return removeable

	def __is_android(self, path):
		"""
		Check if path has ANDROIDFDCU flag file generated by Android Device
		
		@param path:	Path of device
		"""
		fdcu_file = os.path.join(path, 'ANDROIDFDCU')
		if os.path.exists(fdcu_file):
			return True
		else:
			return False

	def get_label(self, path, default=None):
		"""
		Get label of the path if it have USBFDCU or ANDROIDFDCU flag file
		
		@param path:	Path of the device
		@param default:	Optional default label
		"""
		vol = None
		if default is None or default == "":
			default = "UNKNOWN"
		
# 		fdcu_file = os.path.join(path, 'USBFDCU')
# 		if os.path.exists(fdcu_file):
# 			vol = config.get_usb_config(UsbRepository(path), "general", "usb_name")
# 		
# 		fdcu_file = os.path.join(path, 'ANDROIDFDCU')
# 		if os.path.exists(fdcu_file):
# 			vol = utility.common.get_first_line(fdcu_file)

		if vol is None or vol == "":
			return default
		else:
			return vol
