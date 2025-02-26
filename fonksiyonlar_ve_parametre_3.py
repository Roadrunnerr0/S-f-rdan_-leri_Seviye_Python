#FONKSİYONLAR VE PARAMETRE(*args,**kwargs,ders="25!") - Ders 25.2
def degerleriGöster(**Degerler):
    for anahtar,deger in degerler.items():
        print(anahtar,deger)

degerleriGoster(mert = "Mekatronik", renk = "Kirmizi", yapi = "Dik")