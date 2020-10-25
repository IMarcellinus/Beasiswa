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
        IPK = input("masukkan IPK : ")
        if ("IPK => 3.0"):
            print("SELAMAT ANDA MENDAPATKAN BEASISWA")
        else:
            print("MAAF ANDA KURANG BERUNTUNG")
    print('')
    print('')
