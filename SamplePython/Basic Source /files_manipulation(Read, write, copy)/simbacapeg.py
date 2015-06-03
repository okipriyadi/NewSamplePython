berkas_peg= open("pegawai.txt")
nip = berkas_peg.read(5)
while nip:
		nama = berkas_peg.read(20)
		gaji = berkas_peg.read(8)
		print nip, nama, gaji
		nip = berkas_peg.read(5)
