print("1. Brio - 150.000/hari")
print("2. Avanza - 200.000/hari")
print("3. Fortuner - 350.000/hari")

pilihan = int(input("pilih mobil 1-3 :"))
hari = int(input("masukkkan lama sewa(hari :"))
kupon = input("Masukkan kupon :")

if pilihan == 1:
    mobil = "Brio"
    harga = 150000
elif pilihan == 2:
    mobil = "Avanza"
    harga = 200000
elif pilihan == 3:
    mobil = "Fortuner"
    harga = 350000
else :
    mobil = "Tidak tersedia"
    harga = 0

sewa = harga * hari

if hari > 3:
    asuransi = 25000
else :
    asuransi = 0

subtotal = sewa + asuransi

if subtotal >= 500000:
    diskon1 = subtotal * 10/100
else :
    diskon1 = 0

setelah_diskon = subtotal - diskon1

if kupon == "AMBATUNER":
    diskon2 = setelah_diskon * 5/100
else :
    diskon2 = 0

total = setelah_diskon - diskon2

print("jenis mobil :", mobil)
print("Lama sewa :", hari)
print("subtotal1 :", subtotal)
print("Diskon1 :", diskon1)
print("Diskon2 :", diskon2)
print("Total bayar :", total)