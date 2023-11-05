produk = [
    {
        "kode":"A123",
        "nama":"Biskut Harimau",
        "harga":20000
    },
    {
        "kode":"A124",
        "nama":"Air Al Mineral",
        "harga":25000
    },
    {
        "kode":"A125",
        "nama":"Mie Instant Mantap",
        "harga":2000
    },
    {
        "kode":"A126",
        "nama":"Sosis Sofar",
        "harga":3200
    },
]

for i in produk:
    print(i["kode"])
    print(type(i))

jumlah_total = 0
for x in produk:   
    jumlah_total +=x["harga"]
print(jumlah_total)
print(type(jumlah_total))
