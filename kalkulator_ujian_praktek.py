def tambah(a, b):
    return a + b
def kurang(a, b):
    return a - b
def kali(a, b):
    return a * b
def bagi(a, b):
    if b == 0:
        return "Tidak bisa membagai dengan angka nol!"
    else:
        return a / b
    
while True:
    angka1 = float(input("masukkan angka pertaman: "))
    angka2 = float(input("masukkan angka kedua: "))
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print(f"\n")
    print("= = = = = = = = = =    Selamat datang diaplikasi kalkulator     = = = = = = = = = =")
    print("= = = = = = = = = =                 Pilihan Opsi!               = = = = = = = = = =")
    print(f"\n")
    print("1. penambahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    print(f"5. keluar\n")
    
    o = input("Silahkan masukkan angka(1-5): ")
    
    if o == '1':
        print ("anda memilih penjumlahan")
        print("hasil penjumlahan dari inputan pertama dan kedua adalah: ", tambah(angka1, angka2))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        
        print(f"\n")
    elif o == '2':
        print ("anda memilih pengurangan")
        print("hasil penguranagn dari inputan pertama dan kedua adalah: ", kurang(angka1, angka2))
        print(f"\n")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    elif o == '3':
        print ("anda memilih perkalian")
        print("hasil perkalian dari inputan pertama dan kedua adalah: ", kali(angka1, angka2))
        print(f"\n")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    elif o == '4':
        print ("anda memilih pembagian")
        print("hasil pembagian dari inputan pertama dan kedua adalah: ", bagi(angka1, angka2))
        print(f"\n")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    elif o == '5':
        print(f"\n")
        print (" - - - - - - - - - -  Terimakasih telah menggunakan kalkulator  - - - - - - - - - - ")
        break
    else:
        print(f"\n")
        print (" - - - - - - - - -   pilihan tidak vailid. silahkan coba lagi!   - - - - - - - - - - ")
        
        
        
        