file=open("db-inventory.txt","a")
while True:
    bertanya = input("Input Data Inventory Baru Yes/No ?")
    print("*********************************************")
    if bertanya == "Yes" or bertanya == "yes":
        Namaperangkat= input("Nama perangkat :")
        lokasi=input("Lokasi :")
    elif bertanya == "No" or bertanya == "no":
        print ("selesai")
        break
   
    file.write(Namaperangkat + lokasi +"\n")
file.close()
isi=[]
file=open("db-inventory.txt","r")
for item in file:
    item=item.strip()
    isi.append(item)

file.close()
print(item)

        