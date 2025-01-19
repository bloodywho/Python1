
kisi = {"isim": " Mehmet", "yas": 21 }

kisi["id"]=12345
#del kisi["id"] Silme Komutu

print(kisi)

kisi.update({"isim" : " Ahmet", "yas": 22}) # Toplu bir þekilde dict i deðiþtirmeye yarar.

print(kisi.keys()) 
print(kisi.values())

#for x in kisi: 
#    print(kisi[x])          Burasý direkt valuelarý yazdýrýr yukarýdaki kisi.values() ile ayný.           


#for k in kisi.items():          ('isim', ' Ahmet')
#    print(k)                    ('yas', 22)
#                                ('id', 12345) 

print(kisi.get("cinsiyet","Bulunamadi")) #Dictin içinde var mý yok mu diye kontrol ederiz. 