#Soal1
print('\n----Ubah Celcius ke Fahrenheit ----')
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))


#Soal2
print('\n----Mencari Bilangan Genap ----')
def is_genap(BilanganGenap):
    return BilanganGenap %2 == 0

print(is_genap(4))
print(is_genap(7))


#Soal3
print('\n----Mencetak  Nilai Kelulusan ----')
def Nilai_Kelulusan(Nilai):
    if Nilai >= 80:
        return 'Lulus'
    else :
        return 'Gagal'

print(Nilai_Kelulusan(80))
print(Nilai_Kelulusan(60))


#Soal4
print('\n----Mencetak Bilangan Ganjil ----')
def Bil_Ganjil(Angka):
    for i in range (1, Angka, 2):
        print(i, end=" ")
    
Bil_Ganjil(20)