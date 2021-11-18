# Latihan1
### Sourcecode program
<p> print ("------------------")
<p> print ("Pertemuan ke 7")
<p> print ("latihan 1")
<p> print ("------------------")

<p> print ("menampilkan n bilangan acak yang lebih kecil dari 0.5")

<p> jumlah = int (input("masukkan nilai n :"))
<p> import random
<p> for i in range (jumlah) :

<p>    print ("data ke ", 1+i,"=>",(random.uniform(0.1,0.5))) 

<p>
  
### Penjelasan algoritma
  
<p> 
<p> 1. Masukan nilai N : 5.
<p> 2. Gunakan for range (untuk mengulang data dari 1-5).
<p> 3. Cetak data dan memasukan (random.uniform kurang dari 0.5).
<p> 4. Jika selesai RUN/jalankan programnya.

<p>
  
### Screenshot hasil program
  
<p>
  
![screenshotlatihan1](https://user-images.githubusercontent.com/92582081/141266498-08c08f71-fb50-4a5a-813e-59f520aae651.PNG)

  
  
# Latihan2
### Sourcecode program
<p> print ("------------------")
<p> print ("Pertemuan ke 7")
<p> print ("latihan 2")
<p> print ("------------------")

<p> print ("menampilkan bilangan terbesar dari N buah data yang diinputkan")

<p> max = 0
<p> while True:
<p>    a=int(input("masukkan bilangan :"))
<p>    if max < a :
<p>        max=a
<p>    if a ==0:
<p>        break
<p>print ("\n bilangan terbesar adalah:", max)

<p>

### Penjelasan algoritma  

<p> 1. Masukan max=0
<p> 2. Gunakan while True (untuk perulangan tak terbatas. jika bilangan tersebut bukan nol ,maka akan terus berulang ).
<p> 3. Gunakan if (jika memasukan bilangan nol maka perulangan akan berhenti).
<p> 4. Selanjutnya,gunakan if (untuk mencari nilai max = bilangan terbesar,lalu run/jalankan programnya).

<p>
  
### Screenshot hasil program

<p>
  
![screenshotlatihan2](https://user-images.githubusercontent.com/92582081/141602274-9e2bd6d4-53ba-454e-b89a-8860bcdb0c37.PNG)

<p>

# Program1
### Sourcecode program
<p> print ("------------------")
<p> print ("Pertemuan ke 7")
<p> print ("program 1")
<p> print ("------------------")

<p> print ("jumlah laba hasil investasi seorang pengusaha selama 8 bulan")
<p> print ("------------------")
<p> x=int(input("uang muka :"))

<p> a=0*x 
<p> b=0*x
<p> c=0.01*x
<p> d=0.01*x 
<p> e=0.05*x 
<p> f=0.05*x 
<p> g=0.05*x 
<p> h=0.03*x

<p> y=[a, b, c, d, e, f, g, h]
<p> for i in range (len(y)):
<p>    print("laba bulan ke -",i+1,"sebesar:", y[i])
<p> z= (a+b+c+d+e+f+g+h)
<p> print ("-------------------")
<p> print ("jumlah laba selama 8 bulan adalah:",z)
<p> print ("-------------------")

<p>
  
### Penjelasan Algoritma

<p> 1. Masukkan nilai a.
<p> 2. Gunakan for untuk perulangan dari 1 sampai 8
<p> 3. Lalu gunakan if pertama untuk menentukan laba bulan ke 1 dan ke 2, masukan variabel (b) kalikan nilai (a) dengan data bulan 1 dan 2, cetak (x) dan (b).
<p> 4. Lalu gunakan if kedua untuk menentukan laba bulan ke 3 dan ke 4, masukan variabel (b) kalikan nilai (a) dengan data bulan 3 dan 4, cetak (x) dan (c).
<p> 5. Lalu gunakan if ketiga untuk menentukan laba bulan ke 5 sampai ke 7, masukan variabel (b) kalikan nilai (a) dengan data bulan 5 sampai 7, cetak (x) dan (d).
<p> 6. Lalu gunakan if keempat untuk menentukan laba bulan ke 8, masukan variabel (b) kalikan nilai (a) dengan data bulan 8, cetak (x) dan (e).
<p> 7. Lalu total keseluruhan.
<p> 8. Cetak total.

<p>

### Screenshot hasil program

<P>
  
![screenshotprogram1](https://user-images.githubusercontent.com/92582081/141602338-ea8198a8-856e-4aa1-be8d-5a41bec13324.PNG)
