# Kullanýcýdan isim ve telefon numarasý bilgisi alýnýr
name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")

# 1. Ýsmin uzunluðunu hesaplama
print(f"Isminizin uzunlugu {len(name)} dir.")

# 2. Ýsmin baþýnda veya sonunda gereksiz boþluklar varsa temizleyelim
name = name.strip()  # Baþ ve sondaki boþluklar kaldýrýlýr
print(f"Boþluklar kaldýrýldýktan sonra isim: '{name}'")

# 3. Ýsmin büyük/küçük harf dönüþümleri
print(f"Büyük harflerle isim: {name.upper()}")
print(f"Küçük harflerle isim: {name.lower()}")
print(f"Baþ harfi büyük olacak þekilde isim: {name.capitalize()}")
print(f"Her kelimenin baþ harfi büyük: {name.title()}")

# 4. Ýsmin içinde boþluk olup olmadýðýný kontrol edelim
if " " in name:
    space_index = name.find(" ")  # Ýlk boþluðun indeksini bul
    print(f"Ýsimde {space_index}. indekste bir boþluk var.")
else:
    print("Ýsimde hiç boþluk yok.")

# 5. Telefon numarasýndaki belirli karakterleri deðiþtirme
phone_number = phone_number.replace("-", " ")  # "-" yerine boþluk koy
print(f"Telefon numarasý düzenlendi: {phone_number}")

# 6. Telefon numarasýndaki boþluk sayýsýný kontrol et
space_count = phone_number.count(" ")  # Boþluklarý say
print(f"Telefon numarasýnda {space_count} adet boþluk var.")

# 7. Ýsmin tamamen alfabetik olup olmadýðýný kontrol et
if name.isalpha():
    print("Ýsminiz yalnýzca harflerden oluþuyor.")
else:
    print("Ýsminiz harfler dýþýnda karakterler içeriyor (örneðin boþluk, rakam).")

# 8. Telefon numarasýnýn rakamlardan oluþup oluþmadýðýný kontrol edelim
phone_number_cleaned = phone_number.replace(" ", "")  # Boþluklarý kaldýr
if phone_number_cleaned.isdigit():
    print("Telefon numarasý yalnýzca rakamlardan oluþuyor.")
else:
    print("Telefon numarasýnda rakam dýþýnda karakterler var.")

# 9. Ýsmin baþýnda veya sonunda belirli bir karakter olup olmadýðýný kontrol et
if name.startswith("A"):
    print("Ýsminiz 'A' harfi ile baþlýyor.")
else:
    print("Ýsminiz 'A' harfi ile baþlamýyor.")

if name.endswith("z"):
    print("Ýsminiz 'z' harfi ile bitiyor.")
else:
    print("Ýsminiz 'z' harfi ile bitmiyor.")

# 10. Ýsmi merkezleme ve özel karakterlerle süsleme
centered_name = name.center(30, "*")  # Ýsmi 30 karakter geniþliðinde ortalar, boþluk yerine "*" koyar
print(f"Ortalanmýþ isim: {centered_name}")

# 11. Telefon numarasýný zfill ile düzenleme (baþýna sýfýr ekleme)
phone_number_with_zeros = phone_number_cleaned.zfill(12)  # 12 karaktere tamamlar
print(f"Telefon numarasý (sýfýr eklenmiþ): {phone_number_with_zeros}")
