w = input("Masukkan kata : ")
num = len(w) 

if (num == 7) :
    print ("Huruf tengah pada kata", w, "adalah", w[2:5])
elif (num == 3) :
    print ("Huruf tengah pada kata", w, "adalah", w[1])
elif (num == 6) :
    print ("Huruf tengah pada kata", w, "adalah", w[2:4])
elif (num == 8) :
    print ("Huruf tengah pada kata", w, "adalah", w[2:6])
elif (num == 9) :
    print ("Huruf tengah pada kata", w, "adalah", w[3:6])
else:
    print ("wadidaw")