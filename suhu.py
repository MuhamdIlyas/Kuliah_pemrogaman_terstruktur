#program suhu
print ' '
print '-----'
print ' '

ruangan = raw_input ('\tMasukkan Nama Ruangan: ')
suhu = int (input ('\tMasukkan Suhu Ruangan: '))
print ' '
print '\tCetak'
print '\tNama Ruangan:',ruangan
if (suhu <=20 ):
    print "\tKeterangan :Suhu Ruangan Dingin"
else:
    print "\tKeterangan :Suhu Ruangan Panas"
