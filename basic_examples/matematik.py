class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2

    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2

matematik = Matematik()
sonucCikarma= matematik.cikar(20,10)
print("sonuç:" + str(sonucCikarma))
sonucToplama = matematik.topla(3,5)
print("sonuç:" + str(sonucToplama))