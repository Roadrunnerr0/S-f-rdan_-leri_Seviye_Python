from itertools import permutations

# Sabit ilk iki hane
fixed_start = "05"

# Geri kalan 9 hanede bulunması gerekenler
required_digits = [5, 5, 4, 4, 9, 9]

# Ekstra 3 hane için 0-9 arası rakamları içeren bir liste
extra_digits = list(range(10))

# İlk 50 sonucu saklayacağımız liste
results = []

# Kombinasyonları üret
for extra_combination in permutations(extra_digits, 3):
    # Geri kalan 9 haneyi oluştur
    full_digits = required_digits + list(extra_combination)
    
    # Tüm permütasyonları hesapla
    for perm in set(permutations(full_digits)):
        number = fixed_start + ''.join(map(str, perm))
        results.append(number)
        
        # İlk 50 sonucu al ve işlemi durdur
        if len(results) == 50:
            break
    if len(results) == 50:
        break

# Sonuçları yazdır
print("İlk 50 örnek:")
for number in results:
    print(number)