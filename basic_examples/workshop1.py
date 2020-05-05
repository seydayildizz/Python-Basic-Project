sayi1 = 10
sayi2 = 20
sayi3 = 25


print("En büyük sayı : " + str(sayi3))

# 5! hesaplamasını yapınız.. 5! = 5*4*3*2*1

sayi = int(input("Kaçın faktöriyelini hesaplayayım : "))

fac = 1
if sayi<0:
    print("Negatif sayıların faktöriyeli hesaplanamaz")

elif sayi==0:
    print("Sonuc : 1")

else:
    for i in range(1,sayi+1):  # 5 dahil olsun diye +1  yazılır
        fac = fac * i
        print("Sonuç : " , fac)

#1=1*1
#1=1*2
#2=2*3
#6=6*4
#24=24*5
#120