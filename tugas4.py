

#menentukan umur manusia
nama= "Ramura"
umur= 18
#cetak data umur manusia
if(umur >= 0 and umur <= 18):
    keterangan= "usia dibawah 18 tahun"
elif(umur >= 18 and umur < 65):
    keterangan= "usia antara 18 dan 65"
elif(umur >= 65 and umur < 100):
    keterangan= "usia diatas 65"
print("Nama Manusia \t:", nama, "\nUmur Manusia \t:", umur, "\nKeterangan \t:", keterangan)
print()
#menentukan angka mana yang lebih besar dan lebih kecil
nilai1= 20
nilai2= 25

if(nilai1 > nilai2):
    hasil= "Nilai 1 lebih besar dari nilai 2"

elif(nilai1 < nilai2):
    hasil= "Nilai 1 lebih kecil dari nilai 2"

#cetak menentukan angka mana yang lebih besar dan lebih kecil
print("Nilai 1 : ", nilai1, "\nNilai 2 : ", nilai2,"\n",hasil )



