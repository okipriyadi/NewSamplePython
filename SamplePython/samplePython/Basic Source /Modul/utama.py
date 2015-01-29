from Bidang import Segitiga, Persegi
sgtgA = Segitiga(3, 9)
prsgA = Persegi(5)
print "Luas Segitiga A : ", sgtgA.HitungLuas()
print "Sisi Miring Segitiga A : ", sgtgA.GetSisiMiring()
print "Keliling Segitiga A : ", sgtgA.HitungKeliling(sgtgA.GetSisiMiring())
print "\n"
print "Luas Persegi A : ", prsgA.HitungLuas()
print "Keliling Segitiga A : ", prsgA.HitungKeliling()