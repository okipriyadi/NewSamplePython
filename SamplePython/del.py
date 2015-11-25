import re
value = "TCV123asd"

number_only = re.search(r'[0-9]+', value).group()
if number_only[0] == "0":
    print ">>>>>1"
    value = re.search(r'[A-z]+', value).group() + number_only[1:]
else:
    value = re.search(r'[A-z]+', value).group() + number_only
    print ">>>>>2"
print value