#====================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1A: Membaca seluruh isi file
#====================================================

# Membaca seluruh isi file
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()

print(isi_file)
print("=========== hasil read ============")
print("tipe data:", type(isi_file))
print("jumlah karakter:", len(isi_file))
print("jumlah baris:", isi_file.count("\n") + 1)

#====================================================
# Membaca file per baris
#====================================================
print("\n======= file per-baris =======")
jumlah_baris = 0

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        if not baris:
            continue
        jumlah_baris += 1
        print("baris ke-", jumlah_baris)
        print("isinya:", baris)

#====================================================
# Memecah data per baris
#====================================================
print("\n=========================================")

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        if not baris:
            continue
        nim, nama, nilai = baris.split(",")
        print("nim:", nim, "| nama:", nama, "| nilai:", nilai)

#====================================================
# Menyimpan ke dalam LIST
#====================================================
print("\n===============================")

data_list = []

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        if not baris:
            continue
        nim, nama, nilai = baris.split(",")
        data_list.append([nim, nama, int(nilai)])

print("======= data mahasiswa dalam list =======")
print(data_list)

print("\n======= jumlah record dalam list =======")
print("jumlah record:", len(data_list))

if len(data_list) > 0:
    print("\n======= contoh record pertama =======")
    print(data_list[0])
else:
    print("data_list kosong")

#====================================================
# Menyimpan ke dalam DICTIONARY
#====================================================
print("\n===============================")

data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        if not baris:
            continue
        nim, nama, nilai = baris.split(",")
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }

print("======= data mahasiswa dalam dictionary =======")
print(data_dict)