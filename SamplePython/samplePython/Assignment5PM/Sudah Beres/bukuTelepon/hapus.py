 for item in self.data:
            if(re.search(keyword, item['nama']) or re.search(keyword, item['alamat']) or re.search(keyword, item['telepon'])):
                print '%-4s%-20s%-35s%-13s' % (item['no'],item['nama'] , item['alamat'] , item['telepon'] )
                hitung = 1