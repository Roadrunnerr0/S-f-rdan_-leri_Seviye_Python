#LIST COMPREHENSION - Ders 21.
kisiler = ["Mustafa,Ali,Tolga,Safa,İrem,Melisa,Azra,Elif"]

m_ile_baslayan = [kisi for kisi in kisiler if "m" in kisi or "M" in kisi]

print(m_ile_baslayan)