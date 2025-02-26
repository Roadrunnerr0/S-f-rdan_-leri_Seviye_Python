#LIST COMPREHENSION - Ders 21.
kisiler = ["Mustafa,Ali,Tolga,Safa,İrem,Melisa,Azra,Elif"]

m_ile_baslayan=[]
for kisi in kisiler:
    if kisi[0] == "m" or kisi[0] == "M":
        m_ile_baslayan.append(kisi)

print(m_ile_baslayan)   
