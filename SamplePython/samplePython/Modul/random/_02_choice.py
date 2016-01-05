from random import choice

text =  "abcABC123"
pilih = choice(text)
print pilih



print ">>>>>>>>>>pilihan banyak"
plaintext = ''.join(map(lambda _: choice(text), range(64)))
print plaintext
print len(plaintext)

print ">>>>>>>>>>alfa_num"
from string import digits, letters
print "digits =", digits
print "letters =", letters
alfa_num = digits + letters
print "alfa_num =", alfa_num

plaintext = ''.join(map(lambda _: choice(alfa_num), range(64)))
print "plainteks =", plaintext
print "lebar plainteks =", len(plaintext)
