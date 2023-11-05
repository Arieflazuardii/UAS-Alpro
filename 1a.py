def bacafile():
    file=open("angka_saya.txt","r")
    isi=file.read()
    print(isi)
    file.close()

bacafile()