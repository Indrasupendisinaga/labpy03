# Latihan1
- Sourcecode program
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
<p>
- Screenshot hasil program
<p> 
 ![screenshotlatihan1](https://user-images.githubusercontent.com/92582081/141254122-f7b5d6a9-74e4-4a39-93e4-cd641d0dcf2e.PNG)


# Latihan2
- Sourcecode program
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


# Program1
- Sourcecode program
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
