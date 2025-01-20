# Temel bir s�n�f tan�m�
class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def ses_cikar(self):
        return "Ses ��kar�yorum!"  # Polymorphism i�in temel metot

    def __str__(self):
        return f"Hayvan: {self.isim}, Ya�: {self.yas}"


# Kal�t�m (Inheritance): Hayvan s�n�f�ndan t�reyen K�pek s�n�f�
class Kopek(Hayvan):
    def __init__(self, isim, yas, tur):
        super().__init__(isim, yas)  # �st s�n�f�n constructor'�n� �a��rma
        self.tur = tur

    def ses_cikar(self):  # Polymorphism: �st s�n�ftaki metodu ge�ersiz k�lma (override)
        return "Hav hav!"

    def kuyruk_salla(self):
        return f"{self.isim} kuyru�unu sall�yor!"

    def __str__(self):
        return f"K�pek: {self.isim}, Ya�: {self.yas}, T�r: {self.tur}"


# Kal�t�m: Hayvan s�n�f�ndan t�reyen Kedi s�n�f�
class Kedi(Hayvan):
    def __init__(self, isim, yas, cins):
        super().__init__(isim, yas)
        self.cins = cins

    def ses_cikar(self):  # Polymorphism
        return "Miyav!"

    def tirman(self):
        return f"{self.isim} bir a�aca t�rmand�!"

    def __str__(self):
        return f"Kedi: {self.isim}, Ya�: {self.yas}, Cins: {self.cins}"


# Polymorphism'in g�c�n� g�steren bir fonksiyon
def hayvan_sesi(hayvan):
    print(f"{hayvan.isim} diyor ki: {hayvan.ses_cikar()}")


# S�n�flar�n kullan�m�
hayvan1 = Hayvan("Hayvan", 5)
kopek1 = Kopek("Karaba�", 3, "Golden Retriever")
kedi1 = Kedi("Pamuk", 2, "Van Kedisi")

# Temel bilgiler
print(hayvan1)  # ��k��: Hayvan: Hayvan, Ya�: 5
print(kopek1)   # ��k��: K�pek: Karaba�, Ya�: 3, T�r: Golden Retriever
print(kedi1)    # ��k��: Kedi: Pamuk, Ya�: 2, Cins: Van Kedisi

# Polymorphism �rne�i
hayvan_sesi(hayvan1)  # ��k��: Hayvan diyor ki: Ses ��kar�yorum!
hayvan_sesi(kopek1)   # ��k��: Karaba� diyor ki: Hav hav!
hayvan_sesi(kedi1)    # ��k��: Pamuk diyor ki: Miyav!

# �zel metotlar
print(kopek1.kuyruk_salla())  # ��k��: Karaba� kuyru�unu sall�yor!
print(kedi1.tirman())         # ��k��: Pamuk bir a�aca t�rmand�!

