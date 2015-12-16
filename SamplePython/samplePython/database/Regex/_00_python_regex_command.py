"""
Python provides the raw string notation r , with which the backslashes are treated
as normal characters. So, r"\b" is not the backspace anymore; it's just the character \
and the character b , and the same goes for r"\n"

Using raw string is the recommended option following the Python official
"""
import re 
pattern = re.compile(r'<HTML>')
print pattern

print("=================================MATCH========================================")
print pattern.match("<HTML>") #artinya dia match
print pattern.match("<HTML>asd") #artinya dia match
print pattern.match(" <HTML>") #artinya tidak match match
print pattern.match("asd<HTML>") #artinya tidak match match
#it will the same with this
print re.match(r'<HTML>', "<HTML>")
print re.match(r'<HTML>', " <HTML>")
#menmpilkan data
print pattern.match("<HTML>asd<HTML>").group() 
print("=================================SEARCH========================================")
print pattern.search(" <HTML>")#artinya ditemukan
print pattern.search("asd <HTML>")#artinya ditemukan
"""
match = pencariaanya mulai dari awal, jika diawal tidak sama maka akan direturn tidak match
search = dimanapun pattern tersebut berada jika patternanya sama maka akan dianggap ditemukan  
"""
print pattern.search(" <HTML>asdasd<HTML>").group()
print("=================================MATCH WITH POS PARAMETER========================================")
"""
The optional pos parameter specifies where to start searching, as shown in the
following code:
"""
print pattern.match(" <HTML>") #artinya tidak match match
print pattern.match(" <HTML>", 1) #artinya dimulai dari huruf indeks ke 1, hasilnya match


print("=================================SUBTITUTE========================================") 
s = "how much for the maple syrup? $20.99? That's ricidulous!!!"
print s
#ganti semua simbol dengan spasi
s = s = re.sub(r'[^0-9a-zA-Z]+', ' ', s)
print s

print("=================================Find ALL========================================") 
s = "how much for the maple syrup? $20.99? That's ricidulous!!!"
print s
#ganti semua simbol dengan spasi
s  = re.findall(r'u', s)
print s