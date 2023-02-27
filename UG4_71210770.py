import json

jmlh_barang = int(input("Masukkan jumlah barang = "))

barang_list = []



for j in range(jmlh_barang):
    nama_barang = input(f"Nama barang {j+1} = ")
    harga_barang = int(input(f"Harga barang {j+1} = "))
    barang = {"nama": nama_barang, "harga": harga_barang}
    barang_list.append(barang)

total_hrg = sum(barang["harga"] for barang in barang_list)

datafile = {"total": total_hrg, "barang": barang_list}

with open("barang.json", "r") as f:
    json.dump(datafile, f, indent=4)