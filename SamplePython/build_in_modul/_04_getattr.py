"""
Objects in Python can have attributes. For example you have an object person, 
that has several attributes: name, gender, etc. You access these attributes 
(be it methods or data objects) usually writing: person.name, person.gender, 
person.the_method(), etc.

But what if you don't know the attribute's name at the time you write the program? 
For example you have attribute's name stored in a variable called gender_attribute_name
"""
class Hello_world():
    def __init__(self):
        self.Pariabel = "saya orang sunda"
        
    def saja(self):
        print "pulangkan saja "
    
a = Hello_world()
b = getattr(a, "Pariabel")
print b

c = getattr(a, "saja")
c()


