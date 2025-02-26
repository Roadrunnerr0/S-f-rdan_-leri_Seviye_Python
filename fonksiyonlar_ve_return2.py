#FONKSİYONLAR VE RETURN - Ders 24

def sayiteksedondur_ciftiseosayiyakadartopla(sayi):
    if sayi%2==1:
        return sayi
    
    toplam = 0
    for i in range(1,sayi+1):
        toplam +=i
    return toplam 

print(sayiteksedondur_ciftiseosayiyakadartopla(210))
