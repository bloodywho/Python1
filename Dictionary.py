
kisi = {"isim": " Mehmet", "yas": 21 }

kisi["id"]=12345
#del kisi["id"] Silme Komutu

print(kisi)

kisi.update({"isim" : " Ahmet", "yas": 22}) # Toplu bir �ekilde dict i de�i�tirmeye yarar.

print(kisi.keys()) 
print(kisi.values())

#for x in kisi: 
#    print(kisi[x])          Buras� direkt valuelar� yazd�r�r yukar�daki kisi.values() ile ayn�.           


#for k in kisi.items():          ('isim', ' Ahmet')
#    print(k)                    ('yas', 22)
#                                ('id', 12345) 

print(kisi.get("cinsiyet","Bulunamadi")) #Dictin i�inde var m� yok mu diye kontrol ederiz. 