import json

def write_json(nama_maha,hobi_maha,prestasi, filename = 'mahasiswa.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data.append(nama_maha)
        file_data[nama_maha]["Biodata"].append({"Hobi" :"%s"%(hobi_maha[0]),
        "Prestasi" : prestasi})
        json.dump(file_data, file, indent = 4)

input_data = int(input("Masukkan jumlah mahasiswa baru : "))
for i in range(0,input_data):
    count = 1
    nama_maha = input("Masukkan nama Anda : ")
    jml_hobi_maha = int(input("Masukkan Jumlah hobi : "))
    hobi_maha = dict()
    for j in range(0,jml_hobi_maha):
        hobi_maha[j] = input("Masukkan hobi ke-%d : "%(count))
        count += 1
    prestasi_maha = input("Masukkan Prestasi Anda : ")
    print("====Data berhasil dimasukkan====")
write_json(nama_maha,hobi_maha,prestasi_maha)

