#Program Pengaturan Suhu Ruangan
print '  '

print '\t====================================================='
print '\t########## Program Pengaturan Suhu Ruangan ##########'
print '\t====================================================='

username = raw_input('\t\t\tMasukkan Username :')
password = raw_input('\t\t\tMasukkan Password :')
username_form_db = "latihan" or "Latihan"
password_form_db = "123456789"

print ' '
if username == username_form_db :
    if password == password_form_db :
        print '\tUsername dan Password yang Anda Masukkan Berjodoh'
    else:
        print '\tUsername dan Password yang Anda Masukkan Belum Berjodoh'
else:
    print '\tUsername dan Password yang Anda Masukkan Belum Berjodoh'

    print ' '

ruangan = raw_input ("\tMasukkan Nama Ruangan : ")
suhu    = int(input ("\tMasukkan Suhu Ruangan : "))
print ' '
print "\tCetak"
print "\tNama Ruangan          :",ruangan
if (suhu <=28 ):
    print "\tKeterangan            : Suhu Dalam Ruangan",ruangan + " " + "Dingin"
else:
    print "\tKeterangan            : Suhu Dalam Ruangan",ruangan + " " + "Panas"

print ' '
print '\t===== Terima Kasih Anda Telah Menggunakan Aplikasi Ini ====='

