print("=======Program Manipulasi String=======")
print("Pilihan Menu : ")
print ("1. Hitung kata ")
print ("2. cek kata ")
print ("3. ubah kata ")
n= input("Pilihan anda : ")

#1
def hitungKata():
    k1= input(" Masukkan sebuah kalimat/kata : ")
    numhitung= input("Masukkan kata yang ingin dihitung : ")
    lowernum1= k1.lower()
    lowernum2= numhitung.lower()
    if lowernum2 in lowernum1:
        o= lowernum1.count(lowernum2)
        print("Terdapat sebanyak",o,"kata",numhitung,"di dalam string")
#2
def cekkata():
    num1= input("Masukkan sebuah kalimat/kata : ")
    numcek= input("Masukkan kata yang ingin di cek : ")
    if numcek in num1:
        print("kata",numcek,"terdapat di dalam string")
        print("String diubah menjadi : ")
        n = num1.replace(numcek,numcek.upper())
        print(n)
    
    else:
        print("Kata",numcek,"tidak terdapat di dalam string ")
        print("String diubah menjadi : ")
        print(num1,numcek)
#3
def ubahKata():
    num2= input("Masukkan sebuah kalimat/kata : ")
    numcek2= input("Masukkan kata yang ingin di ubah : ")
    numganti= input("Masukkan kata pengganti :")
    print("Anda akan mengubah kata",numcek2,"menjadi",numganti,"sebanyak 1x")
    cek= input("Apakah anda ingin mengubah jumlah total penggantian kata ? (yes/no) : ")
    if cek=="no":
        print("String berhasil diubah menjadi : ")
        print(num2.replace(numcek2,numganti,1))

    elif cek== "yes":
        jumlahdiganti= int(input("Masukkan jumlah total penggantian : "))
        print("String berhasil diubah menjadi : ")
        print(num2.replace(numcek2,numganti,jumlahdiganti))
if n == "1":
    hitungKata()

elif n == "2" :
    cekkata()

elif n == "3" : 
    ubahKata()

else:
    print("Pilihlah yang ada dimenu!")