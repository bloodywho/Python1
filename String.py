# Kullan�c�dan isim ve telefon numaras� bilgisi al�n�r
name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")

# 1. �smin uzunlu�unu hesaplama
print(f"Isminizin uzunlugu {len(name)} dir.")

# 2. �smin ba��nda veya sonunda gereksiz bo�luklar varsa temizleyelim
name = name.strip()  # Ba� ve sondaki bo�luklar kald�r�l�r
print(f"Bo�luklar kald�r�ld�ktan sonra isim: '{name}'")

# 3. �smin b�y�k/k���k harf d�n���mleri
print(f"B�y�k harflerle isim: {name.upper()}")
print(f"K���k harflerle isim: {name.lower()}")
print(f"Ba� harfi b�y�k olacak �ekilde isim: {name.capitalize()}")
print(f"Her kelimenin ba� harfi b�y�k: {name.title()}")

# 4. �smin i�inde bo�luk olup olmad���n� kontrol edelim
if " " in name:
    space_index = name.find(" ")  # �lk bo�lu�un indeksini bul
    print(f"�simde {space_index}. indekste bir bo�luk var.")
else:
    print("�simde hi� bo�luk yok.")

# 5. Telefon numaras�ndaki belirli karakterleri de�i�tirme
phone_number = phone_number.replace("-", " ")  # "-" yerine bo�luk koy
print(f"Telefon numaras� d�zenlendi: {phone_number}")

# 6. Telefon numaras�ndaki bo�luk say�s�n� kontrol et
space_count = phone_number.count(" ")  # Bo�luklar� say
print(f"Telefon numaras�nda {space_count} adet bo�luk var.")

# 7. �smin tamamen alfabetik olup olmad���n� kontrol et
if name.isalpha():
    print("�sminiz yaln�zca harflerden olu�uyor.")
else:
    print("�sminiz harfler d���nda karakterler i�eriyor (�rne�in bo�luk, rakam).")

# 8. Telefon numaras�n�n rakamlardan olu�up olu�mad���n� kontrol edelim
phone_number_cleaned = phone_number.replace(" ", "")  # Bo�luklar� kald�r
if phone_number_cleaned.isdigit():
    print("Telefon numaras� yaln�zca rakamlardan olu�uyor.")
else:
    print("Telefon numaras�nda rakam d���nda karakterler var.")

# 9. �smin ba��nda veya sonunda belirli bir karakter olup olmad���n� kontrol et
if name.startswith("A"):
    print("�sminiz 'A' harfi ile ba�l�yor.")
else:
    print("�sminiz 'A' harfi ile ba�lam�yor.")

if name.endswith("z"):
    print("�sminiz 'z' harfi ile bitiyor.")
else:
    print("�sminiz 'z' harfi ile bitmiyor.")

# 10. �smi merkezleme ve �zel karakterlerle s�sleme
centered_name = name.center(30, "*")  # �smi 30 karakter geni�li�inde ortalar, bo�luk yerine "*" koyar
print(f"Ortalanm�� isim: {centered_name}")

# 11. Telefon numaras�n� zfill ile d�zenleme (ba��na s�f�r ekleme)
phone_number_with_zeros = phone_number_cleaned.zfill(12)  # 12 karaktere tamamlar
print(f"Telefon numaras� (s�f�r eklenmi�): {phone_number_with_zeros}")
