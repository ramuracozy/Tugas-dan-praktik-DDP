class hewan:
    def __init__(self,nama, makanan, habitat, kembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.kembangbiak = kembangbiak

    def cetak(self):
        print("\nSaya adalah hewan",self.nama,"\nsaya makan",self.makanan,"\nhabitat saya di",self.habitat,"\nSaya berkembang biak dengan cara",self.kembangbiak)

class Badak(hewan):
    def __init__(self, nama, makanan, habitat, kembangbiak, tipe_tanduk, hewan_dilindungi):
        super().__init__(nama, makanan, habitat, kembangbiak)
        self.tipe_tanduk = tipe_tanduk
        self.hewan_dilindungi = hewan_dilindungi

    def cetak(self): 
        super().cetak()
        print("tipe tanduk saya adalah",self.tipe_tanduk,"\nsaya adalah hewan yang",self.hewan_dilindungi)

class Ikan(hewan):
    def __init__(self, nama, makanan, habitat, kembangbiak,Tipe_air, bernafas):
        super().__init__(nama, makanan, habitat, kembangbiak)
        self.Tipe_air = Tipe_air
        self.bernafas = bernafas

    def ikan(self):
        super().cetak()
        print("Saya berenang di air",self.Tipe_air,"\nSaya Bernafas dengan",self.bernafas)

class Ular(hewan):
    def __init__(self, nama, makanan, habitat, kembangbiak,racun,berjalan):
        super().__init__(nama, makanan, habitat, kembangbiak)
        self.racun = racun
        self.berjalan = berjalan

    def Ular(self):
        super().cetak()
        print("Saya adalah hewan yang",self.racun,"\nSaya Berjalan dengan",self.berjalan)

# objek badak
badak = Badak("Badak","rumput","Hutan tropis","Melahirkan","Bercula satu","Dilindungi")
badak.cetak()

# objek Ikan
ika_mas = Ikan ("Ikan Mas","Cacing","Air","Memijah","Air Tawar","Insang")
ika_mas.ikan()

# objek ular
Cobra = Ular ("Ular Cobra","Tikus","Tanah","Bertelur","Berbisa","Melata")
Cobra.Ular()