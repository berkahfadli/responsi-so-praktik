print("="*10)
print("\tmanajen ram dalam komputer")
print("="*10)

Ram = int(input("masukan kapasitas total ram\t: "))
petabit = int(input("masukan kapasitas total petabit\t: "))
blok = 2
print("="*10)
sistemoperasi = int(input("masukan kapasitas ram yang digunakan sistemoperasi \t: "))
kapasitas_Ram1 = int(input("masukan kapasitas ram yang digunakan program 1\t: "))
kapasitas_Ram2 = int(input("masukan kapasitas ram yang digunakan program 2\t: "))

petabit = (Ram / petabit)
proter = (sistemoperasi + kapasitas_Ram1 + kapasitas_Ram2)
protdk = (Ram - sistemoperasi - kapasitas_Ram1 - kapasitas_Ram2)
jumlahblok = (kapasitas_Ram1 + kapasitas_Ram2) / petabit

print("output :")
print("total RAM\t :",Ram)
print("total petabit\t :",petabit)
print("total kapasitas per petabit\t :",petabit)
print("total RAm terpakai\t\t :",petabit)
print("total Ram tidak terpakai\t :",proter, "Gbps")
print("total blok yang bernilai 1\t :",protdk, "Gbps")
print("total blok yang bernilai 2\t :",jumlahblok)
print("total blok yang bernilai 0\t :",blok - jumlahblok)
print("="*10)