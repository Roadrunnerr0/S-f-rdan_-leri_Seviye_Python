#print(), file ve flush parametresi 
dosya= open("MetinBelgesi.txt","w") # burada bir dosya açtık ve içine bil metin belgesi yazdık en sondaki "w" ise yazı işlemi için kullanıldığını söylüyor
print("Mustafa Erdogan",file=dosya)