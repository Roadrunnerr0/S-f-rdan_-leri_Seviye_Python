#CLASS(SINIF) Yapısı Nedir? - 👩🏽‍💻 👨🏽‍💻Python Programlama - Ders 29
class Araba():
    def __init__(self,marka,model,fiyat,rent):
        self.gelenMarka = marka
        self.gelenModel = model
        self.gelenFiyat = fiyat
        self.gelenRenk = Renk

    def bilgileriyazdir():
        print(self.gelenMarka,self.gelenModel,self.gelenFiyat,self.gelenRenk)

araba1 = Araba("Renault","Clio","40000","Mavi")
araba2 = Araba("Ford","Fiesta","30000","Kirmizi")

araba1.bilgileriYazdir()
araba2.bilgileriYazdir()