#Latihan Program Kasir
print " "
import datetime
import time
now=datetime.datetime.now()
tanggal=now.date()
waktu=now.time()

d_kd={"001":"001","002":"002","003":"003","004":"004"}
d_kode={"001":"Pensil","002":"Buku","003":"Bolpoin","004":"Penghapus"}
d_data={"Pensil":"1000","Buku":"3000","Bolpoin":"2000","Penghapus":"500"}

d_harga=[]
d_barang=[]
d_jumlah=[]
d_total=[]
i_0
kop="""
\t============================================================
\t##################### Toko Semoga Bisa #####################
\t##################### Jl. Motivator 07 #####################
\t============================================================
"""

username = raw_input("Masukkan Username :") 
password = raw_input("Masukkan Password :")
username_from_db = "pentingnulis" or "Penting Nulis"
password_from_dn = "sakmetune" or "Sakmetune"

def menu ():
    print kop
    print """
\t\t\t ;"; MENU ;";
\t\t<_________________>
\t\t\t1.
