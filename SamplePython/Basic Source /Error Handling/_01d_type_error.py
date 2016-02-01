"""
Raised when an operation or function is applied to an object of inappropriate type. 
The associated value is a string giving details about the type mismatch.
"""
from base64 import b64decode

try: 
    payload = "Ih6AQ/LkejZGr2DmAY/CdJrmuMIYXqW+peWBZ3y+3n+XWadXbw/CFSg+Jge2mSczxejwx39BGIsjw6o9Ok3m7g=="
    decoded1 = b64decode(payload)
    print "decode1 = ",decoded1
    
    payload2 ="aabbcc"
    decoded2 = b64decode(payload2)
    print "decode2", decoded2

except TypeError as e:
    print "========="
    print "error =>", e