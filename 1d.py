def tulis_angka(angka):
    x=open("angka_saya.txt", "a")
    x.write(str(angka)+ "\n")

tulis_angka(angka=15)