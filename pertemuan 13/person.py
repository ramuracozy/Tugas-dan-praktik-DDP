class orang:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def makan(self):
        print("saya bisa makan")

    def cetak(self):
        print("nama saya",self.fname,self.lname)

class mahasiswa(orang):
    def __init__(self, fname, lname, prodi, angkatan):
        super().__init__(fname, lname)
        self.prodi = prodi
        self.angkatan = angkatan

    def cetak(self):
        super().cetak()
        print("saya prodi",self.prodi,"angkatan",self.angkatan)

class Pegawai(orang):
    def bekerja(self):
        print("saya bekerja")

# objek orang
x  = orang("Bagus","maulana")
x.cetak()

# objek mahasiswa
y = mahasiswa("Dwi","Astuti","Teknik Informatika",2023)
y.cetak()
y.makan()

# objek Pegawai 
agus = Pegawai("Agus", "Rahman")
agus.bekerja()