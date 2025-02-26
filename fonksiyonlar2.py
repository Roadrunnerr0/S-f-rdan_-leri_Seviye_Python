#FONKSİYONLAR- Ders 23.1
def ebob(a,b):
    enkucuksayi = min(a,b)
    enbuyokortakbolen = 1

    for i in range(1,enkucuksayi+1):
        if a % i == 0 and b % i== 0:
            enbuyokortakbolen = i
    
    print(f"{a} ve {b} nin en büyük ortak böleni:  {enbuyokortakbolen} dir.")

ebob(50,200)