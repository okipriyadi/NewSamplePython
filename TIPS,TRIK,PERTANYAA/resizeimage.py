import os, sys
from PIL import Image

for filename in os.listdir("."):
   exten = filename.split(".",)
   
   if exten[-1] == "jpeg" or exten[-1] == "png" or exten[-1] == "jpg":
        from io import BytesIO
        import os

        THUMBNAIL_SIZE = (250, 250)
	
        DJANGO_TYPE = exten[-1]
        
        if DJANGO_TYPE == 'jpeg' or DJANGO_TYPE == 'jpg' or DJANGO_TYPE[0] == 'jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'png' or DJANGO_TYPE[0] == 'png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

	print "filename: ",filename
        image = Image.open(filename)
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
	image.save(filename, PIL_TYPE)

