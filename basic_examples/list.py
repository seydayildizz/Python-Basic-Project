
urunler = ["Laptop", "Mouse", "Keyboard"]
print(urunler)
print(type(urunler))
urunler.append("Telefon")
urunler[0] = "Hoparlör"
print(urunler)

ogrenciler1 = ["Engin", "Şeyda", "Gökhan"]
ogrenciler2 = ["Baran", "Enes", "Aykut"]


ogrenciler1 = ogrenciler2
ogrenciler2[0] = "Zehra"  # öğrenciler2'nin 0. elemanı değişti
print(ogrenciler1)
print(ogrenciler2)

sayi1 = 10
sayi2 = 20
sayi1 = sayi2
sayi2 = 60
print(sayi2)

#referans tip -> list, class
#değer tip -> int

isim  = "şeyda"
print(isim[0])

bosListe = []  #devops developer operations( geliştirme operasyonları)

