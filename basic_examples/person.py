class Person:
    def __init__(self,name,lastname): #constructor method
        self.ad = name
        self.soyad = lastname



musteri1 = Person("Şeyda" , "Zenler")
musteri2 = Person("Gökhan" , "Yıldız")
musteri3 = Person("Zehra" , "Burak")

print(musteri1.ad + musteri2.ad + musteri3.ad)
print(musteri1.soyad +musteri2.soyad + musteri3.soyad)
