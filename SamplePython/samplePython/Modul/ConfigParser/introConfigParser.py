import ConfigParser


Config = ConfigParser.ConfigParser() #atau bisa juga dengan perintah Config = ConfigParser.RawConfigParser()
print "ConfigParser.ConfigParser()", Config
"""Explanation: We first import the configparser, 
   tell it to read the file, and get a listing of the sections. 
   Sections are listed in square brackets []."""
print "Config.read() : ",Config.read("tommorow.ini")
#print section dalam dokumen
print "Config.section():",Config.sections()

#Config.option untuk mendapatkan key
#Config.get("parametersection", key)
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            print "option/key : ", option
            dict1[option] = Config.get(section, option)
            print "value : ", dict1[option] 
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

i = ConfigSectionMap("SectionOne")
print "print i:", i

Name = ConfigSectionMap("SectionOne")['name']
Age = ConfigSectionMap("SectionOne")['age']
print "Hello %s. You are %s years old." % (Name, Age)

print ConfigSectionMap("SectionOne")['single']
#-> ini akan mengakibatkan error karna hasil keluaran ConfigSectionMap adalah string bukan bolean print int(ConfigSectionMap("SectionOne")['single'])
#to get boolean value you can use Config.getboolean(section, option)
single = Config.getboolean("SectionOne", "single")

print single
print int(single)


