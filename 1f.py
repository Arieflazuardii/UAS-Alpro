def tulis_angka(angka):
    x=open("angka_saya.txt", "a")
    x.write("\n"+str(angka))

tulis_angka(angka=input("Masukkan Angka :"))

