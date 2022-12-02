print=('======= Program Manipulasi String =======')

menu=('Pilihan Menu :')
menu=('1.Hitung Kata')
menu=('2.Ubah Kata')
menu = input('Pilihan anda : ')

def hitung():
    kalimat = input('masukan sebuah kalimat /kata :')
    hit = input('Masukan Kata yang ingin di hitung :')
    a = kalimat.count(hit)
    menu =('Terdapat sebanyak', a, 'kata', hit,'didalam kalimat')
    return a

def ubah():
    kalimat = input('Masukan sebuah kalimat kata : ')
    mana = input ('Masukan kata yang ingin di ubah : ')
    pengganti = input('Masukan kata pengganti :')

    ganti = kalimat.replace(mana,pengganti)

    print(f'String Berhasil Diubah menjadi {ganti}')
    return ganti 

if menu == '1' :
    hitung()
elif menu == '2' :
    ubah()
else :
    print('Pilihan yang anda input tidak terdaftar di daftar pilihan')