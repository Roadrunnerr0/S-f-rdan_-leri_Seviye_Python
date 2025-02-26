#Sen Kodla!- Ders 26 (Yapildi)
while True:    
    def tamsayibölenleridondur(sayi):
        bosliste =[]

        for i in range(1,sayi):
            if sayi % i == 0: 
                bosliste.append(i)
    
        return bosliste     
    gelensayi = int(input("Sayiyi giriniz: "))
    print(tamsayibölenleridondur(gelensayi))