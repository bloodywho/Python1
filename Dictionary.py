# S�zl�k tan�m�
kisi = {"isim": "Mehmet", "yas": 21}

# Yeni bir anahtar-de�er �ifti ekleme
kisi["id"] = 12345

# Bir anahtar-de�eri silme (�rne�in, `id` anahtar�n�)
# del kisi["id"]

# S�zl��� g�ncelleme (toplu olarak)
kisi.update({"isim": "Ahmet", "yas": 22})

# S�zl���n anahtarlar�n� ve de�erlerini yazd�rma
print("Anahtarlar:", kisi.keys())  # dict_keys(['isim', 'yas', 'id'])
print("De�erler:", kisi.values()) # dict_values(['Ahmet', 22, 12345])

# T�m s�zl��� anahtar-de�er �iftleri olarak yazd�rma
for k, v in kisi.items():
    print(f"{k}: {v}")  # �rnek ��kt�: isim: Ahmet, yas: 22, id: 12345

# Bir anahtar�n varl���n� kontrol etme (Varsa de�erini, yoksa varsay�lan bir mesaj d�nd�rme)
print("Cinsiyet:", kisi.get("cinsiyet", "Bulunamad�"))

# Varsay�lan bir de�erle ekleme: E�er anahtar yoksa ekle, varsa de�i�tirme
kisi.setdefault("meslek", "��renci")
print("Meslek:", kisi["meslek"])  # ��k��: Meslek: ��renci

# S�zl���n uzunlu�unu bulma
print("S�zl�kteki toplam eleman say�s�:", len(kisi))  # ��k��: 4

# S�zl��� bir anahtar�n varl���na g�re kontrol etme
if "isim" in kisi:
    print(f"Ki�inin ismi: {kisi['isim']}")  # ��k��: Ki�inin ismi: Ahmet

# T�m de�erleri listeye �evirme
deger_listesi = list(kisi.values())
print("De�erler listesi:", deger_listesi)  # ��k��: ['Ahmet', 22, 12345, '��renci']

# Bir anahtar� kald�rma ve de�erini alma
id_degeri = kisi.pop("id", "Anahtar bulunamad�")
print("ID de�eri:", id_degeri)  # ��k��: ID de�eri: 12345

# S�zl��� temizleme
# kisi.clear()
# print("Temizlenmi� s�zl�k:", kisi)  # ��k��: {}

# �rnek: �� i�e ge�mi� s�zl�k (Nested Dictionary)
kisi["adres"] = {"sehir": "�stanbul", "posta_kodu": "34000"}
print("Adres bilgisi:", kisi["adres"]["sehir"])  # ��k��: �stanbul

# Son hali
print("Son S�zl�k:", kisi)
