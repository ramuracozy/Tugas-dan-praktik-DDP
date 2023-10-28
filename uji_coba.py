#deklarasi dan inisialisasi variabel
pelanggan= "Reza Sitompul"
totalbelanja= 175000

#struktur kendala if
if(totalbelanja > 100000):
    keterangan= "Selamat Anda mendapatkan hadiah"
else:
    keterangan= "Terimakasih sudah berbelanja"

#cetak data
print("Pelanggan", pelanggan,"\n Total Belanja Anda Rp.", totalbelanja,"\n", keterangan)

#Siswa dinyatakan lulus minimal 75 nilainya
nama= "Agus Susilo"
matkul= "MIPA"
nilai= 67.99
#ternary
keterangan= "Lulus" if nilai >= 75 else "Tidak Lulus"

#cetak data
print("Nama Mahasiswa \t:", nama, "\nMata Kuliah \t:", matkul, "\nKeterangan \t:", keterangan)

#Akumulasi nilai mahasiswa
name= "Agung Santoso"
matkul= "Matkom"
nilai= 70
#uji grade dengan IF multi kondisi
if(nilai >= 85 and nilai <= 100):
    grade= "A"
elif(nilai >= 75 and nilai < 85):
    grade= "B"
elif(nilai >= 60 and nilai < 75):
    grade= "C"
elif(nilai >= 30 and nilai < 60):
    grade= "D"
else:
    grade= "E"
#cetak data
print("Nama Mahasiswa \t:", nama, "\nMata Kuliah \t:", matkul, "\nGrade \t:", grade)
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

cuaca = input("apakah cuaca pada hari ini?")

match cuaca:
    case "panas":
        print("ke kampus memakai mobil")
    case "hujan":
        print("ke kampus memakai jas hujan")
    case "badai":
        print("tidak berangkat ke kampus")
    case _:
        print("tetap berangkat ke kampus")

a = int(input("masukan bil1?")) #5
b = int(input("masukan bil2?")) #7
c = a + b
print(c)
nilai=[23, 45, 65, 5, 5, 5, 5, 75, 90, 85, 5, 5, 5, 5, 5]
print(sum(nilai))
print(len(nilai))
print(max(nilai))
print(min(nilai))
print(nilai.count(5))
print(nilai.index(5))

#testting
pilihan = input("""
        ***pilih operasi***
        1. Hitung persegi
        2. Hitung lingkaran
        3. Hitung segitiga
        masukkan pilihan:
        """)
match pilihan:
    case "1":
        s=int(input("masukkan sisi: "))
        persegi=s*s
        print("luas persegi", persegi)
    case "2":
        phi=3.14
        r=int(input("masukkan jari jari: "))
        lingkaran=phi*r*r
        print("luas lingkaran", lingkaran)
    case "3":
        l=1/2
        a=int(input("masukkan alas: "))
        t=int(input("masukkan tinggi: "))
        segitiga=l*a*t
        print("luas segitiga", segitiga)
    case _:
        print("pilihan tidak tersedia")