# edit_data.py
"""
Basically we just have to query the tables to get the artist or album that we want to modify. 
The first two queries do the same thing, but one is shorter than the other. 
This is because peewee provides a shortcut method for doing queries. 
To actually change the record, we just set the returned object's properties to something else.
In this case, we changed the band's name from "Kutless" to "Beach Boys".

The last query demonstrates how to create a SQL join that allows us get a match across 
two tables. This is great if you happen to own two CDs with the same title but you 
only want the query to return the album associated with the band called "Newsboys".

"""
 
import peewee
from _01_create_database import Album, Artist
 
#Jika Kutless tidak ada maka akan error
band = Artist.select().where(Artist.name=="Kutless").get()
 
# shortcut method
band = Artist.get(Artist.name=="Kutless")
print band.name
 
# change band name
band.name = "Beach Boys"
band.save()
 
album = Album.select().join(Artist).where(
    (Album.title=="Thrive") & (Artist.name == "Newsboys")
    ).get()
    
"""
These queries a little hard to follow, so you can break them up into smaller pieces. Here's one example:

query = Album.select().join(Artist)
qry_filter = (Album.title=="Step Up to the Microphone") & (Artist.name == "Newsboys")
album = query.where(qry_filter).get()
"""
    
album.title = "Step Up to the Microphone"
album.save()