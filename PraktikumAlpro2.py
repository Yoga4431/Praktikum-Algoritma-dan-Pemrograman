try:
    angka = int(input("Masukkan sebuah angka: "))
    
    if angka % 2 == 0:
        print(angka, "adalah angka genap.")
    else:
        print(angka, "adalah angka ganjil.")
        
except ValueError:
    print("Input yang dimasukkan bukan angka. Mohon masukkan angka yang valid.")


