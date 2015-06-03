for nomor in [1,2,"tiga",4,5]:
    print nomor
    
tabel = [
            [1, "dua", 3],
            ["siji",2,"telu"],
            ["hiji","dua", "tiga"]
        ]
    
for nomor in tabel :
    print nomor
    
print "bandingkan dengan for yg ini\n"

for nomor in tabel :
    for number in nomor:
        print number
    print "\n"
    
    
for nomor in range(3) : #range menghasilkan daftar bilangan sesuai paramater, dalam hal ini nomber = [0,1,2]]
    print nomor
    
for nomor in range(1,3) : #range menghasilkan daftar bilangan sesuai paramater, dalam hal ini nomber = [0,1,2]]
    print nomor
