a = "   000002312331"
a = str(int(a))
print a

print"==kasus lain =="
a = "sadda00012334asdds"
import re
number_only = str(int(re.search(r'[0-9]+', a).group()))
a = re.search(r'[A-z]+', a).group() + number_only
print a