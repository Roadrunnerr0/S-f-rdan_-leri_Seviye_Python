from random import randint 
oyun_durumu = True 

while oyunDurumu:
    rastgeleSayi = randint(1,100)
    hak = 7
    while True:

        if hak>0:
            tahmin = int(input("Sizce sayi kac {}",format(rastgeleSayi)))
        else:
            print("Sayiyi tahmin edemediniz (Sayi {}".format(rastgeleSayi))
            break
        if tahmin != rastgeleSayi:
            hak -=1
            if tahmin > rastgeleSayi:
                print("Sayi aşağıda kalan tahmin hakkiniz : {}".format(hak))
            else:
                print("Sayi yukarida kalan tahmin hakkiniz: {}".format(hak))
        else:
            print("Teprikler sayiyi tahmin ettiniz")

            break
    
    kontrol = input("Oyuna devam etmek istiyormusunuz (E/H): ")
    if kontrol == "E":
        oyundurumu = True
    else:
        oyundurumu = False