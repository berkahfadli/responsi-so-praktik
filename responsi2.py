import os
listprogram = []

def fungsi(waktu_selesai,porsi,programlist):
    start = 0
    while start < waktu_selesai:
        for i,data in enumerate(programlist):
            proses = data[0]
            waktu_proses = data[1]
            waktu_sisa = waktu_proses - porsi
            
            if(waktu_proses >= porsi):
                print(proses,'-> Detik Ke -',start, ' s.d. - Detik Ke -', start + porsi )
            else:
                print(proses,'-> Detik Ke -',start, ' s.d. - Detik Ke -', start + waktu_proses )
            
            if(waktu_proses >= porsi):
                start += porsi
            else:
                start += waktu_proses
                
            if( waktu_sisa > 0):
                listprogram.append([proses,waktu_sisa])

os.system("cls")
total_proses = int(input('Total Proses : '))

for i in range(total_proses):
    proses = input('Nama Proses : ')
    print("")
    waktu = int(input('Waktu Pemrosesan : '))
    print("")
    data_list = [proses,waktu]
    listprogram.append(data_list)

porsi = int(input('porsi Waktu : '))

time_complete = 0
for i in listprogram:
    time_complete += i[1]

print("")
fungsi(time_complete,porsi,listprogram)