class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembang_biak
    def cetak(self):
        print("Nama \t\t:", self.nama,
        "\nmakanan \t:", self.makanan,
        "\nhidup \t\t:", self.hidup, 
        "\nberkembang biak :", self.berkembangbiak) 
object = Animal("Ikan", "Pelet", "Air", "bertelur")  
object.cetak()
        