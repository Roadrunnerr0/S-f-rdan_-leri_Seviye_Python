#RANGE() - Ders 19
sayi = int(input("Sayi giriniz: "))
sayac = 2
asal_sayilar = [] # liste objesi aldık 

while sayi>0: #yazdığımız sayı 0 dan büyükm,
    asal_sayilar.append(sayi) #yazdımığız sayı sıfırdan büyükse listeye sokalım
    while sayi > sayac: #yazdığımız sayı sayac dan büyükse wihle içine alalım 
        if sayi % sayac == 0: #yazdığımız sayı sayaca tam bölünüyormu
            asal_sayilar.remove(sayi) # yazdığımız sayı tam bölünüyorsa sayaca o sayıyı çıkaralım
            break
        sayac +=1  #sayacı bir arttırıp tekrar yazdığımız sayıy oraya koyalım eğer tam bölünüyorsa while dan çıkarız 
    
    sayac = 2 #tekrar başlarken saacı yeniden 2ye çekelim
    sayi -=1 #sayiyida başladığımız değerden bir azaltalım
print(asal_sayilar)