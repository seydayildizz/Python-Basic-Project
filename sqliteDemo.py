import sqlite3


def listele():
    baglanti = sqlite3.connect("chinook/chinook.db")  #bağlantı adresi
    cursor = baglanti.execute("select FirstName,LastName from customers") #sorguyu çalıştır

    for satir in cursor:
        print(satir[1])

    baglanti.close()

listele() #listeleme yapar