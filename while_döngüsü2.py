#WHILE döngüsü - Ders 18
import random #random importu çağırdık 
yaziGelen =0
turaGelen =0

parayuzeyi =["Tura","Yazi"] # bir list objesi uyguladık 

atilacakpara =int(input("Kaç kere para atmak istiyorsunuz"))

while atilacakpara > 0:
    paraüstü =random.choice(parayuzeyi) #yazdığımız list objesinden rastgele bir eleman seçecek

    if paraüstü == "Tura":
        turaGelen +=1
        print("Tura Geldi: ")
    else:
        yaziGelen +=1
        print("Yazi Geldi: ")
    
    atilacakpara -=1 #her yapılan işlemden sonra atışı bir azalatacak 
print("Tura sayisi:{}\nYazi Sayisi:{}".format(turaGelen,yaziGelen)) 