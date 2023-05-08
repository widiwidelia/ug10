# __class__ -> underscore -> dunder -> double underscore

'''
id_en = dict() #satu arah #urutan tidak penting
dir(id_en) #untuk mengurai isi type
id_en['makan'] = 'eat'
id_en['belajar'] = 'study'
id_en['minum'] = 'drink'

print(id_en)
print(id_en.keys())
print(id_en.values())

del id_en['belajar'] #menghapus key & value 'belajar'
#hanya boleh menyebut key dalam mengedit
'''

'''
khs = {
    '71200183' : ['Tekkom', 'Jarkom', 'Logmat'],
    '71193450' : ['Tekkom', 'PAK', 'Logmat']
    #sebelah kiri (key) berisi str atau int
    #sebelah kanan (value) bebas
    #1 kunci 2 value ga bisa, 2 kunci 1 value bisa
    #tidak ada limitasi
}

print(khs['71200183'])
print(khs['71200183'][0]) #yang pertama saja

for key in khs.keys():
    print(f"NIM: {key}, Matkul: {khs[key]}")

# menambahkan mata kuliah ke dalam value
khs['71193450'].append("IMK")
print(khs['71193450'])

# menghapus mata kuliah dari value
del khs['71200183'][0] #menghapus "Tekkom"
print(khs['71200183'])
'''

'''
def tabel_pangkat(n, pangkat):
    hasil = dict() #membuat dictionary

    for i in range(1,n+1): #mengisi key
        hasil[i] = i ** pangkat #mengisi value
    return hasil

n = int(input("Masukkan n: "))
pangkat = int(input("Masukkan pangkat: "))
hasil = tabel_pangkat(n,pangkat)
print(hasil)
'''

'''
#mengambil unique values
#array/list of dictionary
data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
        {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},
        {"VIII":"S007"}]
hasil = []
for d in data: #looping isi list
    for value in d.values(): # ambil value
        if hasil.count(value) == 0: #kalau belum ada di list,
            hasil.append(value) #append

print(hasil)
'''

# menyusun dictionary yang menyusun isi kartu keluarga

kk = {
    # 'Nomor_KK' : ['7308180205083848'],
    'Kepala_Keluarga' : 'Mingyu',
    'Anggota' : [
        {'Nama' : 'Gyu', 'Agama' : 'Kristen', 'Status_1' : 'Nikah', 'Status_2' : 'Kepala Keluarga', 'Status_3' : 'WNA', 'Tahun' : int(1997)},
        {'Nama' : 'Jen', 'Agama' : 'Katolik', 'Status_1' : 'Nikah', 'Status_2' : 'Istri', 'Status_3' : 'WNI', 'Tahun' : int(1997)},
        {'Nama' : 'Chan', 'Agama' : 'Hindu', 'Status_1' : 'Belum', 'Status_2' : 'Anak', 'Status_3' : 'WNI', 'Tahun' : int(2001)}
    ],
}

print(f"Kepala keluarga: {kk['Kepala_Keluarga']}")
print(f"Jumlah anggota keluarga: {len(kk['Anggota'])}")
# print(f"Nama dan agamanya: {kk['Agama']}")
# print(f"Yang sudah menikah: {kk['Anggota']}")
print("\n Agama masing-masing:")
for agama in kk['Anggota']:
    print(f"{agama['Nama']} = {agama['Agama']}")

print("\n Yang sudah menikah: ")
for status_1 in kk['Anggota']:
    if status_1['Status_1'] == 'Nikah':
        print(f"{status_1['Nama']}")

print("\n Yang merupakan anak: ")
for status_2 in kk['Anggota']:
    if status_2['Status_2'] == 'Anak':
        print(f"{status_1['Nama']}")

print("\n Yang merupakan WNA: ")
for status_3 in kk['Anggota']:
    if status_3['Status_3'] == 'WNA':
        print(f"{status_3['Nama']}")

print("\n Yang tahun lahirnya > 2000: ")
for tahun in kk['Anggota']:
    if tahun['Tahun'] > 2000:
        print(f"{tahun['Nama']}")