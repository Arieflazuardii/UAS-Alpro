def read_number():
    x=open("angka_saya.txt","r")
    isi=x.read().splitlines()
    isi_int = []
    for i in isi :
        isi_int.append(int(i))
    x.close()
    return isi_int

read_number()

def angka_saya_awal():
    file=open("angka_saya.txt","r")
    isi=file.read().splitlines()
    isi_int = []
    for i in isi :
        isi_int.append(int(i))
    file.close()
    return isi_int

