# tkinter modülünden tüm bileþenleri içe aktarýyoruz
from tkinter import *

# islem adlý fonksiyon tanýmlanýyor
def islem():
    # Yeni bir Tkinter penceresi oluþturuluyor
    pencere = Tk()
    pencere.title("New Programmer")  # Pencerenin baþlýðý belirleniyor

    # Konsola bir mesaj yazdýrýlýyor
    print("Merhaba!!")

    # Ýlk buton oluþturuluyor, týklama iþlemi devre dýþý býrakýlmýþ (state=DISABLED)
    b = Button(
        pencere,
        text="Tikla!",  # Buton üzerindeki yazý
        command=islem,  # Butona týklanýnca tekrar `islem` fonksiyonu çaðrýlýr
        state=DISABLED  # Buton devre dýþý býrakýlmýþtýr
    )

    # Ýkinci buton oluþturuluyor
    b2 = Button(
        pencere,
        text="2. Buton!",  # Buton üzerindeki yazý
        command=islem,  # Butona týklanýnca tekrar `islem` fonksiyonu çaðrýlýr
        bg="white",  # Butonun arka plan rengi
        fg="red",  # Butonun yazý rengi
        borderwidth=8  # Buton kenar geniþliði
    )

    # Ýlk buton pencereye yerleþtiriliyor
    b.pack(pady=20, padx=20, side=LEFT)  # Sol tarafa hizalanýyor ve boþluk býrakýlýyor

    # Ýkinci buton pencereye yerleþtiriliyor
    b2.pack(pady=20, padx=20, side=RIGHT)  # Sað tarafa hizalanýyor ve boþluk býrakýlýyor
    b2.place(x=50, y=10, width=100, height=30)  # Ayrýca belirli koordinatlara yerleþtiriliyor

    # Tkinter ana döngüsünü baþlatýyoruz
    pencere.mainloop()

# `islem` fonksiyonunu çaðýrarak programý baþlatýyoruz
islem()
