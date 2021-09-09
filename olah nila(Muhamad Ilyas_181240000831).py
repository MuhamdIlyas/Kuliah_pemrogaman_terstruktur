# Program Menghitung Nilai Akhir Semester
print ' '

print '\t###############################################################'
print '\t*********** Program Menghitung Nilai Akhir Semester ***********'
print '\t###############################################################'
print ' '

username = raw_input('\t\t\tMasukkan Username :')
password = raw_input('\t\t\tMasukkan Password :')
username_form_db = "Belajar" or "belajar"
password_form_db = "semangat"

print 'Nilai Akhir Semester adalah 25% UTS + 25% UAS + 20% Tugas + 10% Keaktifan + 20% Kehadiran'
print ' '

nama    =raw_input ("Masukkan Nama Mahasiswa   :")
nim     =raw_input ("Masukkan NIM Mahasiswa     :")
makul   =raw_input ("Masukkan Mata Kuliah       :")
uts     =raw_input ("Masukkan Nilai UTS         :")
uas     =raw_input ("Masukkan Nilai UAS         :")
tugas   =raw_input ("Masukkan Nilai Tugas       :")
aktif   =raw_input ("Masukkan Nilai Keaktifan   :")
hadir   =raw_input ("Masukkan Nilai Kehadiran   :")
print " "

nilai_akhir = (0.25*float(uts)) + (0.25*float(uas)) + (0.2*float(tugas)) + (0.1*float(aktif)) + (0.2*float(hadir))                                                                                           
print " "
print "------------------------------------------------------------------------"
print " "
print 'Nilai Akhir Semester'
print 'Nama Mahasiswa               :',nama
print 'NIM Mahasiswa                :',nim
print 'Mata Kuliah                  :',makul
print 'Adalah                       :', float(nilai_akhir)
print 'Nilai dibulatkan menjadi     :', round(nilai_akhir)
print " "

print "------------------------------------------------------------------------"
print "_______________Teatap Semangat dan Belajar Lebih Giat Lagi______________"
print "------------------------------------------------------------------------"
