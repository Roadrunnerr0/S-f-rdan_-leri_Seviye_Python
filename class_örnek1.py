class Personel():
    def  __init__(self,ad,soyad,yas,cinsiyet,maas):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.cinsiyet=cinsiyet
        self.maas=maas
    
    def bilgileriyazdir(self):
        prsint(""" 
{}{} Bilgileri Şunlardir :  
yaş : {}
Cinsiyet: {}
Maaş:{}        
        """.format(self.ad,self.soyad,self.yas,self.cinsiyet,self.maas))
personel = Personel("Mustafa","Erdogan","20","Erkek",60000)
personel.bilgileriyazdir()
