#SİZ KODLAYIN! - if&elif&else - Ders 16(YAPILDI)
Vize = int(input("Vize notunu giriniz: "))
Final = int(input("Final notunu giriniz: "))

a= Vize* 40/100
b = Final *60/100
c= a+b

if 85<=c<=100:
    print("Notunuz AA")
elif 70<=c<85:
    print("Notunuz BA")
elif 60<=c<=70:
    print("Notunuz BB")
elif 50<=c<=60:
    print("Notunuz CB")
elif 40<=c<=50:
    print("Notunz CC")
else:
    print("Notunuz FF")
