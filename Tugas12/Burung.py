from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_kelamin, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_kelamin = jenis_kelamin
        self.jenis = jenis
        
    def cetak_burung(self):
        print("---------------------------------")
        super().cetak()
        print("Jenis Kelamin \t:", self.jenis_kelamin, 
              "\nJenis \t\t:", self.jenis)
        
Kakaktua = Burung("Kakaktua", "Kacang", "Darat & Udara", "Bertelur", "Jantan", "Unggas")
Kakaktua.cetak_burung()

Gagak = Burung("Kakaktua", "Kacang", "Darat & Udara", "Bertelur", "Betina", "Unggas")
Gagak.cetak_burung()