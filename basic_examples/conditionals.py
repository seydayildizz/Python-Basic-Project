istenenKredi = 100000
hesap = 9555
minimumOlmasiGerekenHesap = 10000

if hesap>=minimumOlmasiGerekenHesap:
    print("kredi verilebilir")
    print("ödemeler hesaplandı")
elif hesap>=9000 and hesap<=9500:
    print("Müdüre sorulacak")
elif hesap>=9501 and hesap<=9999:
    print("Genel Müdüre sorulacak")
else:
    print("Kredi almak için bakiyeniz yetersiz")
print("işlem sonu")

