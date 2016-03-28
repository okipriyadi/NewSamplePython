# else hanya dipanggil ketika jika tidak terjadi error yang di jaring oleh except
# sedangkan finally dpanggil baik jika ada error ataupun tidak

try:
    foo = open("foo.txt")
except IOError:
    print("error")
else:
    print(foo.read())
finally:
    print("finished")