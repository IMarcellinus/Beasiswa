#Cara membuat program beasiswa sederhana
pilihan = 1
while pilihan != 0:
    print("1. Beasiswa Prestasi")
    print("2. Beasiswa Bidikmisi/KIP Kuliah")
    print('')

    pilihan = int(input("Masukkan Pilihan : "))
    print('')
    
    if pilihan==1:
        nama = input("Masukkan Nama : ")
        IPK = input("Masukkan IP : ")
        if float(IPK >= 3.0):
            print("SELAMAT ANDA BERHAK MENDAPATKAN BEASISWA PRESTASI")
        else:
            print("MOHON MAAF ANDA BELUM BERUNTUNG SILAHKAN COBA KEMBALI TAHUN DEPAN :)")
    if pilihan==2:
        nama = input("Masukkan Nama : ")
        gaji_ortu = input("Masukkan Gaji Orang Tua : ")
        if int(gaji_ortu <= 1000000):
            print("SELAMAT ANDA BERHAK MENDAPATKAN BEASISWA BIDIKMISI/KIP KULIAH")
            print('')
        else:
            print("MOHON MOHON MAAF ANDA BELUM BERUNTUNG SILAHKAN COBA KEMBALI TAHUN DEPAN :)")
            print('')
