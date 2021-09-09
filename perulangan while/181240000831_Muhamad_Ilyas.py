#Tugas 4

print "         ****************************************************************************"
print "         ........ Program UAS Menggunakan Perulangan While dengan Inputan ..........."
print "         ****************************************************************************"
print ""
print ""

makanan = raw_input("\tMasukkan Makanan Kesukaan Anda                    :")
minuman = raw_input("\tMasukkan Minuman Kesukaan Anda                    :")
print ""
print ""
cetak_makanan  = int(raw_input("\tMasukkan berapa kali pencetakan Makanan Kesukaan  :"))
cetak_minuman  = int(raw_input("\tMasukkan berapa kali pencetakan Minuman Kesukaan  :"))
print ""
print ""
angka = 0
while(angka < int(cetak_makanan)):
    print "\t",makanan
    angka+=1
print ""
print ""

angka = 0
while(angka < int(cetak_minuman)):
    print "\t",minuman
    angka+=1
