# Kullanıcıdan isim ve telefon numarası bilgisi alınır
name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")

# 1. İsmin uzunluğunu hesaplama
print(f"İsminizin uzunluğu {len(name)} dir.")

# 2. İsmin başında veya sonunda gereksiz boşluklar varsa temizleyelim
name = name.strip()  # Baş ve sondaki boşluklar kaldırılır
print(f"Boşluklar kaldırıldıktan sonra isim: '{name}'")

# 3. İsmin başındaki veya sonundaki boşlukları ayrı ayrı kaldırma
lstrip_name = name.lstrip()  # Sadece baştaki boşlukları kaldırır
rstrip_name = name.rstrip()  # Sadece sondaki boşlukları kaldırır
print(f"Başındaki boşluklar kaldırıldı: '{lstrip_name}'")
print(f"Sondaki boşluklar kaldırıldı: '{rstrip_name}'")

# 4. İsmin büyük/küçük harf dönüşümleri
print(f"Büyük harflerle isim: {name.upper()}")
print(f"Küçük harflerle isim: {name.lower()}")
print(f"Baş harfi büyük olacak şekilde isim: {name.capitalize()}")
print(f"Her kelimenin baş harfi büyük: {name.title()}")

# 5. İsmin içinde boşluk olup olmadığını kontrol edelim
if " " in name:
    space_index = name.find(" ")  # İlk boşluğun indeksini bul
    print(f"İsimde {space_index}. indekste bir boşluk var.")
else:
    print("İsimde hiç boşluk yok.")

# 6. Telefon numarasındaki belirli karakterleri değiştirme
phone_number = phone_number.replace("-", " ")  # "-" yerine boşluk koy
print(f"Telefon numarası düzenlendi: {phone_number}")

# 7. Telefon numarasındaki boşluk sayısını kontrol et
space_count = phone_number.count(" ")  # Boşlukları say
print(f"Telefon numarasında {space_count} adet boşluk var.")

# 8. İsmin tamamen alfabetik olup olmadığını kontrol et
if name.isalpha():
    print("İsminiz yalnızca harflerden oluşuyor.")
else:
    print("İsminiz harfler dışında karakterler içeriyor (örneğin boşluk, rakam).")

# 9. Telefon numarasının rakamlardan oluşup oluşmadığını kontrol edelim
phone_number_cleaned = phone_number.replace(" ", "")  # Boşlukları kaldır
if phone_number_cleaned.isdigit():
    print("Telefon numarası yalnızca rakamlardan oluşuyor.")
else:
    print("Telefon numarasında rakam dışında karakterler var.")

# 10. İsmin tamamen alfanümerik olup olmadığını kontrol edelim
if name.isalnum():
    print("İsminiz yalnızca harf ve rakamlardan oluşuyor.")
else:
    print("İsminizde özel karakterler veya boşluklar var.")

# 11. Telefon numarasının alfanümerik olup olmadığını kontrol et
if phone_number.isalnum():
    print("Telefon numarası yalnızca harf ve rakamlardan oluşuyor.")
else:
    print("Telefon numarası harf, rakam dışındaki karakterler içeriyor.")

# 12. İsmin başında veya sonunda belirli bir karakter olup olmadığını kontrol et
if name.startswith("A"):
    print("İsminiz 'A' harfi ile başlıyor.")
else:
    print("İsminiz 'A' harfi ile başlamıyor.")

if name.endswith("z"):
    print("İsminiz 'z' harfi ile bitiyor.")
else:
    print("İsminiz 'z' harfi ile bitmiyor.")

# 15. Örnek: Belirli bir karakteri lstrip veya rstrip ile kaldırma
# Örneğin, kullanıcı isminin başına veya sonuna istemeden "@" veya "#" eklemiş olabilir.
test_name = "@Ali#"
print(f"Orijinal isim: '{test_name}'")
print(f"Başındaki '@' karakteri kaldırıldı: '{test_name.lstrip('@')}'")
print(f"Sondaki '#' karakteri kaldırıldı: '{test_name.rstrip('#')}'")
