# Temel bir sýnýf tanýmý
class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def ses_cikar(self):
        return "Ses çýkarýyorum!"  # Polymorphism için temel metot

    def __str__(self):
        return f"Hayvan: {self.isim}, Yaþ: {self.yas}"


# Kalýtým (Inheritance): Hayvan sýnýfýndan türeyen Köpek sýnýfý
class Kopek(Hayvan):
    def __init__(self, isim, yas, tur):
        super().__init__(isim, yas)  # Üst sýnýfýn constructor'ýný çaðýrma
        self.tur = tur

    def ses_cikar(self):  # Polymorphism: Üst sýnýftaki metodu geçersiz kýlma (override)
        return "Hav hav!"

    def kuyruk_salla(self):
        return f"{self.isim} kuyruðunu sallýyor!"

    def __str__(self):
        return f"Köpek: {self.isim}, Yaþ: {self.yas}, Tür: {self.tur}"


# Kalýtým: Hayvan sýnýfýndan türeyen Kedi sýnýfý
class Kedi(Hayvan):
    def __init__(self, isim, yas, cins):
        super().__init__(isim, yas)
        self.cins = cins

    def ses_cikar(self):  # Polymorphism
        return "Miyav!"

    def tirman(self):
        return f"{self.isim} bir aðaca týrmandý!"

    def __str__(self):
        return f"Kedi: {self.isim}, Yaþ: {self.yas}, Cins: {self.cins}"


# Polymorphism'in gücünü gösteren bir fonksiyon
def hayvan_sesi(hayvan):
    print(f"{hayvan.isim} diyor ki: {hayvan.ses_cikar()}")


# Sýnýflarýn kullanýmý
hayvan1 = Hayvan("Hayvan", 5)
kopek1 = Kopek("Karabaþ", 3, "Golden Retriever")
kedi1 = Kedi("Pamuk", 2, "Van Kedisi")

# Temel bilgiler
print(hayvan1)  # Çýkýþ: Hayvan: Hayvan, Yaþ: 5
print(kopek1)   # Çýkýþ: Köpek: Karabaþ, Yaþ: 3, Tür: Golden Retriever
print(kedi1)    # Çýkýþ: Kedi: Pamuk, Yaþ: 2, Cins: Van Kedisi

# Polymorphism örneði
hayvan_sesi(hayvan1)  # Çýkýþ: Hayvan diyor ki: Ses çýkarýyorum!
hayvan_sesi(kopek1)   # Çýkýþ: Karabaþ diyor ki: Hav hav!
hayvan_sesi(kedi1)    # Çýkýþ: Pamuk diyor ki: Miyav!

# Özel metotlar
print(kopek1.kuyruk_salla())  # Çýkýþ: Karabaþ kuyruðunu sallýyor!
print(kedi1.tirman())         # Çýkýþ: Pamuk bir aðaca týrmandý!

