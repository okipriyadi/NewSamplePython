import datetime
import peewee
 
from _01_create_database import Album, Artist
 
new_artist = Artist.create(name="Newsboys")
album_one = Album(artist=new_artist,
                  title="Read All About It",
                  release_date=datetime.date(1988,12,01),
                  publisher="Refuge",
                  media_type="CD")
album_one.save()
 
#multiple input
albums = [{"artist": new_artist,
           "title": "Hell is for Wimps",
           "release_date": datetime.date(1990,07,31),
           "publisher": "Sparrow",
           "media_type": "CD"
           },
          {"artist": new_artist,
           "title": "Love Liberty Disco", 
           "release_date": datetime.date(1999,11,16),
           "publisher": "Sparrow",
           "media_type": "CD"
          },
          {"artist": new_artist,
           "title": "Thrive",
           "release_date": datetime.date(2002,03,26),
           "publisher": "Sparrow",
           "media_type": "CD"}
          ]
 
for album in albums:
    a = Album(**album)
    a.save()
 
bands = ["MXPX", "Kutless", "Thousand Foot Krutch"]
for band in bands:
    artist = Artist.create(name=band)
    artist.save()

#cara lain handle multiple input
albums = [{"artist": new_artist,
           "title": "Hell is for Wimps",
           "release_date": datetime.date(1990,07,31),
           "publisher": "Sparrow",
           "media_type": "CD"
           },
          {"artist": new_artist,
           "title": "Love Liberty Disco", 
           "release_date": datetime.date(1999,11,16),
           "publisher": "Sparrow",
           "media_type": "CD"
          },
          {"artist": new_artist,
           "title": "Thrive",
           "release_date": datetime.date(2002,03,26),
           "publisher": "Sparrow",
           "media_type": "CD"}
          ]
Album.insert_many(albums).execute()

