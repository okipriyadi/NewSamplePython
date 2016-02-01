"""
KeyError akan dipanggil ketika key dalam dictionary tidak diketemukan
"""
try:
    kamus = {'TailNum':'PA-001', 'Nomor':'123'}
    print kamus['TailNum']
    print kamus['Nomor']
    print kamus['ISU']
except KeyError as e:
    print "error key ==>",e, "==>tidak ada"