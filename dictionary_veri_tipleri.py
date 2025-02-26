#Dictionary Veri Tipleri - Ders 10.1
uyeler = {"Uye" : ["Ali","Mehmet","Mustafa","Tolga"],
          "Moderator" : ["Safa", "İrem","Elif"],
          "Yoneticiler" : ["Azra","Buse","Yasemin"]

}
print(uyeler["Uye"]) #burada uyeleri yazdırdık

uyeler["S.moderatorler"] = ["Musa","Sualp"] # burada ise s.moderatorler ekledik listeye
print(uyeler)

uyeler["Uye"].append("Tuğrul") #burada ise append ile uye ye yeni bir eleman ekledik 
print(uyeler["Uye"])

uyeler["Moderator"].remove("Elif") #burada ise moderatorler içerisinden onuru çıkardık 
print(uyeler["Moderator"])

uyeler.clear()
print(uyeler) #bütün dict'i temizler 

kopyaAl= uyeler.copy()#değeri buraya koyalamak
print(kopyaAl)

uyeler.pop("Moderator")#buraya yazılan anahatar kelimeyi kaldırkmak 
print(uyeler )

print(type(uyeler.values()))