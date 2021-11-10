print ("------------------")
print ("Pertemuan ke 7")
print ("latihan 2")
print ("------------------")

print ("menampilkan bilangan terbesar dari N buah data yang diinputkan")

max = 0
while True:
    a=int(input("masukkan bilangan :"))
    if max < a :
        max=a
    if a ==0:
        break
print ("\n bilangan terbesar adalah:", max)