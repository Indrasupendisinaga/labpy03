print ("------------------")
print ("Pertemuan ke 7")
print ("program 1")
print ("------------------")

print ("jumlah laba hasil investasi seorang pengusaha selama 8 bulan")
print ("------------------")
x=int(input("uang muka :"))

a=0*x 
b=0*x
c=0.01*x
d=0.01*x 
e=0.05*x 
f=0.05*x 
g=0.05*x 
h=0.03*x

y=[a, b, c, d, e, f, g, h]
for i in range (len(y)):
    print("laba bulan ke -",i+1,"sebesar:", y[i])
z= (a+b+c+d+e+f+g+h)
print ("-------------------")
print ("jumlah laba selama 8 bulan adalah:",z)
print ("-------------------")
