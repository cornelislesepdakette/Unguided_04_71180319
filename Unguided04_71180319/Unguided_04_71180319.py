import json
data = None
with open('mahasiswa.json','r+') as datafile:
    data = json.load(datafile)

    jumlah = int(input("Masukkan jumlah mahasiswa baru : "))
    for i in range(0,jumlah):
        n_mhs = input("Masukkan nama Anda : ")
        j_pres = int(input("Masukkan Jumlah hobi : "))
        hobi_maha = list()
        hitung = 1
        for isi in range(0,j_pres):
            isi_hobi = input("Masukkan Hobi ke-%d : "%(hitung))
            hobi_maha.append(isi_hobi)
            hitung += 1
        prestasi_mahasiswa = input("Masukkan Prestasi Anda : ")
        isi = {n_mhs:[
            {"Biodata" : {
                "Hobi" : hobi_maha,
                "Prestasi": prestasi_mahasiswa
            }}]}
        print("==== Data berhasil ditambahkan ====")
        data.update(isi)
        datafile.seek(0)
        json.dump(data,datafile,indent=4)

