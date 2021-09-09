#tugas2
print "         -------------------------------------------------------------------"
print "                         Program UAS : Perulangan Menggunakan FOR"
print "         -------------------------------------------------------------------"
print " "
nama = raw_input("\tMasukkan Nama Anda                           :")
almt = raw_input("\tMasukkan Alamat Anda                         :")
wrna = raw_input("\tMasukkan Warna Kesukaan Anda                 :")
print ""
print ""
cetak_nama = int(raw_input("\tMasukkan Berapa Kali Mencetak Nama           :"))
cetak_almt = int(raw_input("\tMasukkan Berapa Kali Mencetak Alamat         :"))
cetak_wrna = int(raw_input("\tMasukkan Berapa Kali Mencetak Warna Kesukaan :"))
print ""
print ""
for i in range(cetak_nama):
    print "\t",nama
print ""
print ""
for i in range(cetak_almt):
    print "\t",almt
print ""
print ""
for i in range(cetak_wrna):
    print "\t",wrna
