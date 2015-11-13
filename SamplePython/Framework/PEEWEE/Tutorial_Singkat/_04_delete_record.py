# del_data.py
 
from _01_create_database  import Artist
 
 
band = Artist.get(Artist.name=="MXPX")
band.delete_instance()