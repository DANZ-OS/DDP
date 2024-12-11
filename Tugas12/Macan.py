from Animal import *

class Macan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, taring):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.corak = corak
        self.taring = taring
        
    def cetak_macan(self):
        print("---------------------------------")
        super().cetak()
        print("Corak \t\t:", self.corak, 
              "\nTaring \t\t:", self.taring)
        
Macan_tutul = Macan("Macan tutul", "Daging", "Darat", "Beranak", "Titik titik", "Tajam")
Macan_tutul.cetak_macan()

Macan_kumbang = Macan("Macan kumbang", "Daging", "Darat", "Bertelur", "Hitam", "Tajam")
Macan_kumbang.cetak_macan()