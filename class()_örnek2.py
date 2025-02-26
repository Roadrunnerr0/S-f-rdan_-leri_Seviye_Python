class Person:
    address = 'no information'

    def __init__(self,name,year):

        self.name = name 
        self.year = year 
        print('init metodu calisir')

p1 = Person(name = 'Mustafa', year =2004)
p2 = Person(name = 'Yagmur', year = 1999)

p1.name ='Mustafa'
p1.address = 'Ankara'

p2.name = 'Yagmur'
p2.address = 'Ankara'

print(f'p1: name: {p1.name} year:{p1.year} address: {p1.address}')
print(f'p1: name: {p2.name} year:{p2.year} address: {p2.address}')


