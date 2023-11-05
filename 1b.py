def read_number_kalidua():
    x=open("angka_saya.txt","r")
    isi = x.read().splitlines()
    for i in isi :
        print(int(i) * 2)
    x.close()

#read_number_kalidua()

def read_angka_kalidua() :
    file=open("angka_saya.txt", "r")
    isi = file.read().splitlines()
    for i in isi:
        print(int(i)*2)
    file.close()

read_angka_kalidua()