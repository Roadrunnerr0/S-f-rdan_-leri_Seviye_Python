#print("Fonksiyonu Ve Özellikleri") 
a = 6
b = "Mustafa"
c = True

print("Mustafa\nerdogan") # alt alta
print("Mustafa\tErdogan") #boşluk bırakarak yana
print(type(a))#cinsini gösterir
print(a,b,c,sep="x") # her değerin arasına x koyar
print(a , end = "--")#end parametresi veriden sonra sonuna konulacak maddeyi verir
print(*a)# harfleri ayrı ayrı yazar
print("{} ile {} toplamı: {} sayısıdır.".format(4,5,9)) # print ile terminale yazıları sonradan koyup, yazdırıyoruz.