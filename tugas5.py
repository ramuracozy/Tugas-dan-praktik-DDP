# Membuat list kendaraan
kendaraan= ["Silvia S15", "Mobil", "2000 cc", "putih",4]
kendaraan.append("Rp.600juta")
kendaraan.append("Sedan")
kendaraan.insert(2,"Nissan")
print(kendaraan) 

# Case menghitung luas bangun datar
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


