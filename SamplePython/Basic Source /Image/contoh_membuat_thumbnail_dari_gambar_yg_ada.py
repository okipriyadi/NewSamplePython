from PIL import Image
from io import BytesIO
import os

THUMBNAIL_SIZE = (250, 250)
a = os.listdir(os.getcwd())
for name in a :
        ext = name.split('.')[-1]
        print name.split('.')[-1]
        PIL_TYPE = ""

        if (name.split('.')[-1] == "jpg" or name.split('.')[-1] == "jpeg" or name.split('.')[-1] == "png" ) and name != "thumbnail": 
                if ext == 'jpeg' or ext == 'jpg':
                    PIL_TYPE = 'jpeg'
                elif ext == 'png' :
                    PIL_TYPE = 'png'
                print "konvert"         
                image=Image.open(name)
                image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
                image.save( 'thumbnail/'+name , PIL_TYPE)