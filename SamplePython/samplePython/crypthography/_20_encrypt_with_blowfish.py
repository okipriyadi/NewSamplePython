'''
Created on Nov 17, 2014

@author: asep

@modifed: andriyanto, Dec 16, 2014
- fix memory error for huge file
'''

#!/usr/bin/env python

import os, sys
from random import randrange
from Crypto.Cipher import Blowfish
from getpass import getpass
import getopt
from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack

class BFCipher:
    def __init__(self, pword):
#         self.__cipher = Blowfish.new(pword)
        print 'init'
        bs = Blowfish.block_size
        iv = Random.new().read(bs)
        self.__cipher = Blowfish.new(pword,Blowfish.MODE_ECB,iv)
        
    def encrypt(self, file_buffer):
        ciphertext = self.__cipher.encrypt(self.__pad_file(file_buffer))
        return ciphertext

    #di pad file di luar
    def encrypt_no_pad(self, file_buffer):
        ciphertext = self.__cipher.encrypt(file_buffer)
        return ciphertext
    
    def decrypt(self, file_buffer):
        cleartext = self.__depad_file(self.__cipher.decrypt(file_buffer))
        return cleartext

    def decrypt_no_depad(self, file_buffer):
        cleartext = self.__cipher.decrypt(file_buffer)
        return cleartext

    # Blowfish cipher needs 8 byte blocks to work with
    def __pad_file(self, file_buffer):
        pad_bytes = 8 - (len(file_buffer) % 8)                                 
        for i in range(pad_bytes - 1): 
            file_buffer += chr(randrange(0, 256))

        # final padding byte; % by 8 to get the number of padding bytes
        bflag = randrange(6, 248); bflag -= bflag % 8 - pad_bytes
        file_buffer += chr(bflag)
        return file_buffer
    def __depad_file(self, file_buffer):
        pad_bytes = ord(file_buffer[-1]) % 8
        if not pad_bytes: pad_bytes = 8
        return file_buffer[:-pad_bytes]
    
    # read file save to buffer
    def readfile(self,filename):
        if os.path.exists(filename):
            data = None
            start = 0
            bufsize = 4*1024*1024*1024
            fsize = os.path.getsize(filename)
#             print 'fsize :',fsize
            f1 = open(filename,'rb')
            f1.seek(start)
            while fsize:
                chunk = min(bufsize,fsize)
                data = f1.read(chunk)
                fsize -= chunk
            f1.close()
            return data
        else:
            print "file '%s' does not exist.\n" % infile
            return None
        pass

    # write buffer to file
    def writefile(self,outbuffer,outfile):
        out_buf = open(outfile,'wb')
        out_buf.write(outbuffer)
        out_buf.close()
        pass
                
    #encrypt method for small file max 100MB
    def encryptfile_s(self,infile,outfile):
        inbuffer = self.readfile(infile)
        if inbuffer is not None:
            outbuffer = self.encrypt(inbuffer)
            self.writefile(outbuffer, outfile)
        pass

    #encrypt method for huge file > 100MB
    def encryptfile(self,filename,enc_filename):
        if os.path.exists(filename):
            data = None
            start = 0
            bufsize = 1024*1024
            fsize = os.path.getsize(filename)
            out_buf = open(enc_filename,'wb')
            f1 = open(filename,'rb')
            f1.seek(start)
            pad_buffer = ''
            while fsize:
                chunk = min(bufsize,fsize)
#                 print 'chunk : ',chunk
                data = f1.read(chunk)

                if chunk == fsize:
                    #pad file
                    pad_bytes = 8 - (fsize % 8)
                    for i in range(pad_bytes - 1): 
                        pad_buffer += chr(randrange(0, 256))
                    # final padding byte; % by 8 to get the number of padding bytes
                    bflag = randrange(6, 248); bflag -= bflag % 8 - pad_bytes
                    pad_buffer += chr(bflag)                #encrypt data
                    #add padding on last data
                    data += pad_buffer
                    
                enc_data = self.encrypt_no_pad(data)
                #write to enc data output
                out_buf.write(enc_data)
                fsize -= chunk
            f1.close()
            out_buf.close()
#             return data
        else:
            print "file '%s' does not exist.\n" % infile
#             return None

    #decrypt method for small file max 100MB
    def decryptfile_s(self,infile,outfile):
        inbuffer = self.readfile(infile)
        if inbuffer is not None:
            outbuffer = self.decrypt(inbuffer)
            self.writefile(outbuffer, outfile)
        pass

    #decrypt method for huge file > 100MB
    def decryptfile(self,filename,dec_filename):
        if os.path.exists(filename):
            data = None
            start = 0
            bufsize = 1024*1024 #per 1Mbyes
            fsize = os.path.getsize(filename)
#             print 'fsize :',fsize
            out_buf = open(dec_filename,'wb')
            f1 = open(filename,'rb')
            f1.seek(start)
            while fsize:
                chunk = min(bufsize,fsize)
#                 print 'chunk : ',chunk
                data = f1.read(chunk)
                if chunk == fsize:
                    #decrypt data
                    dec_data = self.decrypt_no_depad(data)
#                     print 'len dec data b4 :', len(dec_data)

                    #depad file
                    pad_bytes = ord(dec_data[-1]) % 8
                    if not pad_bytes: 
                        pad_bytes = 8
                    
                    dec_data = dec_data[:-pad_bytes]
#                     print 'len data after :', len(dec_data)
                else:
                    #decrypt data
                    dec_data = self.decrypt_no_depad(data)
                #write to enc data output
                out_buf.write(dec_data)
                fsize -= chunk
            f1.close()
            out_buf.close()
            
#             return data
        else:
            print "file '%s' does not exist.\n" % infile
#             return None

'''
    usage:
        key = b'An arbitrarily long key'
        bfc = BFCipher(key)
        bfc.encryptfile('/sync-mgr/acrl/asep.ppk','/sync-mgr/acrl/asep.out')       
        bfc = BFCipher(key)
        bfc.decryptfile('/sync-mgr/acrl/asep.out','/sync-mgr/acrl/asep.in')       

'''

if __name__ == '__main__':
    encrept = BFCipher("bebass")
    encrept.encryptfile_s("/home/kyi/logfile.log","/home/kyi/logfile_enc.log")
    encrept.decryptfile_s("/home/kyi/logfile_enc.log", "/home/kyi/logfile_dec.log")
    encrept.encryptfile("/home/kyi/logfile.log","/home/kyi/logfile_enc2.log")
    encrept.decryptfile("/home/kyi/logfile_enc2.log","/home/kyi/logfile_dec2.log")
    
    """
        def print_usage():
            usage = "Usage: bfc -[e(encrypt) | d(decrypt) | c('cat' like)] infile [outfile]"
            print usage; sys.exit()
    
        def writefile(outfile_name, file_buffer):
            outfile = PrivoxyWindowOpen(outfile_name, 'wb')
            outfile.write(file_buffer)
            outfile.close()
    
        try: opts, args = getopt.getopt(sys.argv[1:], 'e:d:c:')
        except getopt.GetoptError: print_usage()
    
        opts = dict(opts)
        try: mode = opts.keys()[0]
        except IndexError: print_usage()
    
        ifname = opts[mode]
    
        try: ofname = args[0]
        except IndexError: ofname = ifname
    
        if os.path.exists(ifname):
            infile = PrivoxyWindowOpen(ifname, 'rb')
            filebuffer = infile.read()
            infile.close()
        else:
            print "file '%s' does not exist.\n" % ifname
            sys.exit()
    
        key = getpass()
    
        if mode == '-e':
            bfc = BFCipher(key); filebuffer = bfc.encrypt(filebuffer)
            writefile(ofname, filebuffer)
        elif mode == '-d':
            bfc = BFCipher(key); filebuffer = bfc.decrypt(filebuffer)
            writefile(ofname, filebuffer)
        elif mode == '-c':
            bfc = BFCipher(key); sys.stdout.write(bfc.decrypt(filebuffer))
    
        key = 'x'*len(key); del key
    """