#Sen Kodla! - Ders 22 (Yapıldı)
sahipolunanpara = 2000

secim  = input("Karti sokmak icin 's', ayirmak icin 'a' yaziniz: ")

if secim == "s":
    while True:
        islem = int(input("""
         islemler 
         -------------
         1-Para Cekme
         2-Para Yatirma
         3-Hesap bilgileri
         4-Kart iade
         Yapmak istediğiniz islemin nurmarasini giriniz:     
         """))
        if islem == 1:
            cekilmekistenenmiktar = int(input("Cekmek istediğiniz para tutarini giriniz: "))
            if sahipolunanpara <cekilmekistenenmiktar:
                print("Gecersiz islem")
            else:
                sahipolunanpara -= cekilmekistenenmiktar
                print("Sahip olan paraniz: {}".format(sahipolunanpara))
        
        if islem == 2:
            yatirilanmiktar = int(input("Ne kadar para yatirmak istiyorsunuz: "))
            sahipolunanpara += yatirilanmiktar
            print("Sahip olan paraniz: {}".format(sahipolunanpara))
        
        if islem == 3:
            print("Hesap bilgileri:\n***********\nHesap sahibi:Mustafa Erdogan\nHesap IBAN:Tr80 xxxx xxxx xxxxx\nSahip olunan para {}".format(sahipolunanpara))

        if islem == 4: 
            print("karti iade aliniz, Atmden ayrilabilirsiniz.")
            break
    

else:
    print("Atmden ayrildiniz")

