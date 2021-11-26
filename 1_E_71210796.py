#1
def pangkatAngka () : 
    print ("Masukkan angka yang ingin di Pangkatkan")
    num = (float(input("Angka : ")))
    print ("ingin memodifikasi pangkat ?(yes/no)")
    x = input (": ")
    if x == "yes" :
        pangkat = float(input("Masukkan nilai pangkat : "))
        y = float(num**pangkat)
        print ("Hasil dari {0}^{1} = ".format(num,pangkat), y)
    else:
        y = (num**2)
        print ("Hasil dari {0}^2 = ".format(num), y)

#2
def akarBilangan () :
    print ("Masukkan angka yang ingin di Akar")
    bil = (float(input("Angka : ")))
    print ("ingin memodifikasi akar ?(yes/no")
    b = input (": ")
    if b == "yes":
        akar = float(input("Masukkan nilai akar : "))
        r = float(bil**(1/akar))
        print ("Hasil akar pangkat 1 dari {0} = ".format(bil), round(r, 2))
    else:
        r = (bil**0.5)
        print ("Hasil akar pangkat 2 dari {0} = ".format(bil), round(r, 2))

print ("Menu Program Yang Tersedia")
print ("1. pangkatkan angka")
print ("2. akarkan bilangan")

#pilihan 
k = int(input ("Masukkan pilihan yang di inginkan : "))

if k == 1:
    pangkatAngka()
if k == 2:
    akarBilangan()
else: 
    print("-")