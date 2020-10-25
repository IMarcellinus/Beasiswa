#cara membuat program sederhana beasiswa
pilihan = 1
while pilihan != 0 :
    print ("1. Beasiswa Prestasi")
    print ("0. Exit")
    print('')
    print('')
    
    pilihan = int(input("masukkan pilihan anda : "))
    print('')
    if pilihan == 1 :
        nama = input("masukkan nama anda : ")
        ipk = int(input("masukkan IPK : "))
        gaji = int(input("masukkan gaji orang tua : "))
        if gaji >= 100000 and ipk >= 3:
            print("Selamat anda mendapatkan beasiswa", nama)
        else:
            print("Maaf anda kurang beruntung")
    print('')
    print('')
