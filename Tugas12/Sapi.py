from Animal import *

class Hewan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, menghasilkan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.menghasikan = menghasilkan
        
    def cetak_hewan(self):
        print("---------------------------------")
        super().cetak()
        print("Jenis \t\t:", self.jenis, 
              "\nMenghasilkan \t:", self.menghasikan)
        
Sapi = Hewan("Sapi", "Rumput", "Darat", "Beranak", "Mamalia", "Susu")
Sapi.cetak_hewan()

Ayam = Hewan("Ayam", "Beras", "Darat", "Bertelur", "Unggas", "Telur")
Ayam.cetak_hewan()