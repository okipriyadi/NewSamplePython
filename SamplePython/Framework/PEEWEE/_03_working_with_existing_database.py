#If you already have a database, you can autogenerate peewee models using pwiz, 
#a model generator. For instance, if I have a postgresql database named charles_blog, 
#I might run:

#python -m pwiz -e postgresql charles_blog > blog_models.py