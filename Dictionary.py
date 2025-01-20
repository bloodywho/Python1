# Sözlük tanýmý
kisi = {"isim": "Mehmet", "yas": 21}

# Yeni bir anahtar-deðer çifti ekleme
kisi["id"] = 12345

# Bir anahtar-deðeri silme (örneðin, `id` anahtarýný)
# del kisi["id"]

# Sözlüðü güncelleme (toplu olarak)
kisi.update({"isim": "Ahmet", "yas": 22})

# Sözlüðün anahtarlarýný ve deðerlerini yazdýrma
print("Anahtarlar:", kisi.keys())  # dict_keys(['isim', 'yas', 'id'])
print("Deðerler:", kisi.values()) # dict_values(['Ahmet', 22, 12345])

# Tüm sözlüðü anahtar-deðer çiftleri olarak yazdýrma
for k, v in kisi.items():
    print(f"{k}: {v}")  # Örnek çýktý: isim: Ahmet, yas: 22, id: 12345

# Bir anahtarýn varlýðýný kontrol etme (Varsa deðerini, yoksa varsayýlan bir mesaj döndürme)
print("Cinsiyet:", kisi.get("cinsiyet", "Bulunamadý"))

# Varsayýlan bir deðerle ekleme: Eðer anahtar yoksa ekle, varsa deðiþtirme
kisi.setdefault("meslek", "Öðrenci")
print("Meslek:", kisi["meslek"])  # Çýkýþ: Meslek: Öðrenci

# Sözlüðün uzunluðunu bulma
print("Sözlükteki toplam eleman sayýsý:", len(kisi))  # Çýkýþ: 4

# Sözlüðü bir anahtarýn varlýðýna göre kontrol etme
if "isim" in kisi:
    print(f"Kiþinin ismi: {kisi['isim']}")  # Çýkýþ: Kiþinin ismi: Ahmet

# Tüm deðerleri listeye çevirme
deger_listesi = list(kisi.values())
print("Deðerler listesi:", deger_listesi)  # Çýkýþ: ['Ahmet', 22, 12345, 'Öðrenci']

# Bir anahtarý kaldýrma ve deðerini alma
id_degeri = kisi.pop("id", "Anahtar bulunamadý")
print("ID deðeri:", id_degeri)  # Çýkýþ: ID deðeri: 12345

# Sözlüðü temizleme
# kisi.clear()
# print("Temizlenmiþ sözlük:", kisi)  # Çýkýþ: {}

# Örnek: Ýç içe geçmiþ sözlük (Nested Dictionary)
kisi["adres"] = {"sehir": "Ýstanbul", "posta_kodu": "34000"}
print("Adres bilgisi:", kisi["adres"]["sehir"])  # Çýkýþ: Ýstanbul

# Son hali
print("Son Sözlük:", kisi)
