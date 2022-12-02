print('======= Program Manipulasi String =======')

print('Pilihan Menu :')
print('1.Hitung Kata')
print('2.Ubah Kata')
menu = input('Pilihan anda : ')

def hitung():
    kalimat1 = input('masukan sebuah kalimat /kata :')
    hit = input('Masukan Kata yang ingin di hitung :')
    a = kalimat1.count(hit)
    print('Terdapat sebanyak', a, 'kata', hit,'didalam kalimat')
    return a

def ubah():
    kalimat = input('Masukan sebuah kalimat kata : ')
    mana = input('Masukan kata yang ingin di ubah : ')
    pengganti = input('Masukan kata pengganti :')

    ganti = kalimat.replace(mana,pengganti)

    print('String Berhasil Diubah menjadi',ganti)
    return ganti 

if menu == '1' :
    hitung()
elif menu == '2' :
    ubah()
else :
    print('Pilihan yang anda input tidak terdaftar di daftar pilihan')
