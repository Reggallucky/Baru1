print("(L) Lihat\t\t(T) Tambah")
print("===================================================")
print("|NO\t|\tNama\t|\tNIlai\t|\tStatus\t|\t")
print("------------------NO DATA--------------------------")
print("===================================================")
print("(H) Hapus\t\t(U) Ubah")

def Tambah(a,b,c,d):
    f=int(input("Tambah Berapa?\t\t=\t"))
    e=1
    for e in range(e,f):
            b=int(input("Masuakn No Urut\t\t=\t"))
            a=input("Masukan Nama\t\t=\t")
            c=str(input("Masukan Setatus\t\t=\t"))
            if(a=="Akhdan"):
                print("===================================================")
                print("|NO\t|\tNama\t|\tNIlai\t|\tStatus\t|\t")
                print("|",b,"\t|\t",a,"\t|\t",90,"\t|\t",c,"\t|\t")
                print("===================================================")
            else :
                if(a=="Nanang"):
                    print("===================================================")
                    print("|NO\t|\tNama\t|\tNIlai\t|\tStatus\t|\t")
                    print("|",b,"\t|\t",a,"\t|\t",67,"\t|\t",c,"\t|\t")
                    print("===================================================")
            
def Lihat (a,b,c,d):
    a=input("Masukan Nama\t\t=\t")
    if(a=="Akhdan"):
        print("===================================================")
        print("|NO\t|\tNama\t|\tNIlai\t|\tStatus\t|\t")
        print("|",b,"\t|\t",a,"\t|\t",90,"\t|\t",c,"\t|\t")
        print("===================================================")
    else:
        if(a=="Nanang"):
            print("===================================================")
            print("|NO\t|\tNama\t|\tNIlai\t|\tStatus\t|\t")
            print("|",b,"\t|\t",a,"\t|\t",67,"\t|\t",c,"\t|\t")
            print("===================================================")
            
            
def Hapus ():
    print("SELESAI")
    
def Ubah (a,b,c):
    c=str(input("Masukan Setatus\t\t=\t"))
    if(c=="Akhdan"):
        print("===================================================")
        print("|NO\t|\tNama\t|\tNIlai\t|\tStatus\t|\t")
        print("|",b,"\t|\t",a,"\t|\t",90,"\t|\t",c,"\t|\t")
        print("===================================================")
    else :
        if(c=="Nanang"):
            print("===================================================")
            print("|NO\t|\tNama\t|\tNIlai\t|\tStatus\t|\t")
            print("|",b,"\t|\t",a,"\t|\t",67,"\t|\t",c,"\t|\t")
            print("===================================================")
        g=str(input("Ubah ?\t\t = \t"))
        if(g=="Ya"):
            b=int(input("Masuakn No Urut\t\t=\t"))
            a=input("Masukan Nama\t\t=\t")
            c=str(input("Masukan Setatus\t\t=\t"))
            f=int(input("Masukan Niai"))
            print("===================================================")
            print("|NO\t|\tNama\t|\tNIlai\t|\tStatus\t|\t")
            print("|",b,"\t|\t",a,"\t|\t",f,"\t|\t",c,"\t|\t")
            print("===================================================")
            

b=int(input("Masuakn No Urut\t\t=\t"))
a=input("Masukan Nama\t\t=\t")
c=str(input("Masukan Setatus\t\t=\t"))
if(c=="Akhdan"):
        print("===================================================")
        print("|NO\t|\tNama\t|\tNIlai\t|\tStatus\t|\t")
        print("|",b,"\t|\t",a,"\t|\t",90,"\t|\t",c,"\t|\t")
        print("===================================================")
else :
        if(c=="Nanang"):
            print("===================================================")
            print("|NO\t|\tNama\t|\tNIlai\t|\tStatus\t|\t")
            print("|",b,"\t|\t",a,"\t|\t",67,"\t|\t",c,"\t|\t")
            print("===================================================")

d=input("Masuakan Perintah\t\t=\t")
if(d=="L"):
    Lihat(a,b,c,d)
    
if(d=="T"):
    Tambah(a,b,c,d)
    
if(d=="U"):
    Ubah(a,b,c)

if(d=="H"):
    Hapus()