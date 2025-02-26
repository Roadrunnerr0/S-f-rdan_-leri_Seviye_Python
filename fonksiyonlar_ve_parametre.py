#FONKSİYONLAR VE PARAMETRE(*args,**kwargs,ders="25!") - Ders 25

def topla (*sayilar): #değişken bir parametredir ve buraya yazdıklarımız bir list objesidir 
    toplam = 0 
    for sayi in sayilar:
        toplam += sayi
    return toplam 
print(topla(122,134,145,155))

'''
def topla (*sayilar)
    return sum (sayilar) sum fonksiyonu sayilar gibi iteraible alir 
'''