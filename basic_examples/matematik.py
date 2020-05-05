class Matematik:
    def __init__(self, sayi1, sayi2):  # constructor-yapıcı / başlatma yapar
        self.s1 = sayi1  # this gibi
        self.s2 = sayi2  # class seviyesi
        print("Matematik başladı(referansı oluştur)")
        super().__init__()  # base class

    def topla(self):
        return self.s1 + self.s2

    def cikar(self):
        return self.s1 - self.s2

    def bol(self):
        return self.s1 / self.s2

    def carp(self):
        return self.s1 * self.s2


matematik = Matematik(14, 7)
sonuc = matematik.bol()
print("Sonuç: " + str(sonuc))


class Istatistik(Matematik):  # inheritance / Kalıtım
    def __init__(self, sayi1, sayi2):
        super.__init__(sayi1, sayi2)

    def varyansHesap(self):
        return self.s1 * self.s2

istatistik = Istatistik(5, 8)
sonuc = istatistik.varyansHesap()
print("Sonuç:" + sonuc)
