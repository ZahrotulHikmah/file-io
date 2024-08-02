# buka file
#file_pantun = open("pantun.txt", "r")
# baca isi file 
#print (file_pantun.readlines())
# tutup file 
#file_pantun.close()

# buka file
file_pantun = open ("pantun.txt", "r")

# baca isi file
pantun = file_pantun.readlines()

# cetak baris pertama
print(pantun[0])

# cetak baris kedua
print(pantun[1])

# cetak baris ketiga
print(pantun[2])

# cetak baris keempat
print(pantun[3])

# cetak baris kelima
print(pantun[4])

# tutup file 
file_pantun.close()