#Sen kodla!- Ders 26.1 (Yapildi)
def ekok(a,b):
    ekok = a*b

    for sayi in range(ekok,max(a,b)-1,-1):
        if sayi % a == 0 and sayi % b == 0:
            ekok = sayi 
    
    return ekok 

birincisayi = int(input("Birinci sayiyi giriniz: "))
ikincisayi = int(input("İkinci sayiyi giriniz: "))
print(ekok(birincisayi,ikincisayi))
