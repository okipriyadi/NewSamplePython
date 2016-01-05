from zlib import compress

plaintext = "Iya da aku mah apa atuh cuman remeh dina piring "
print "plaintext =", plaintext
print "len dr plaintext", len(plaintext)
dikompres = compress(plaintext)
print "dikompres : ", dikompres
print "len dikompres", len(dikompres)
