"""
KeyError akan dipanggil ketika value dalam dictionary kosong
"""
try:
    kamus = {'TailNum':'PA-001', 'Nomor':''}
    asd = kamus['TailNum']
    qwe = kamus['Nomor']
    print asd
    print qwe
    if not asd : raise ValueError('disini TailNum')
    if not qwe:  raise ValueError('disini Nomor')
except ValueError as e:
    print "error value ==>",e, "==>tidak ada"