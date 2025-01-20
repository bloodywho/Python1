# tkinter mod�l�nden t�m bile�enleri i�e aktar�yoruz
from tkinter import *

# islem adl� fonksiyon tan�mlan�yor
def islem():
    # Yeni bir Tkinter penceresi olu�turuluyor
    pencere = Tk()
    pencere.title("New Programmer")  # Pencerenin ba�l��� belirleniyor

    # Konsola bir mesaj yazd�r�l�yor
    print("Merhaba!!")

    # �lk buton olu�turuluyor, t�klama i�lemi devre d��� b�rak�lm�� (state=DISABLED)
    b = Button(
        pencere,
        text="Tikla!",  # Buton �zerindeki yaz�
        command=islem,  # Butona t�klan�nca tekrar `islem` fonksiyonu �a�r�l�r
        state=DISABLED  # Buton devre d��� b�rak�lm��t�r
    )

    # �kinci buton olu�turuluyor
    b2 = Button(
        pencere,
        text="2. Buton!",  # Buton �zerindeki yaz�
        command=islem,  # Butona t�klan�nca tekrar `islem` fonksiyonu �a�r�l�r
        bg="white",  # Butonun arka plan rengi
        fg="red",  # Butonun yaz� rengi
        borderwidth=8  # Buton kenar geni�li�i
    )

    # �lk buton pencereye yerle�tiriliyor
    b.pack(pady=20, padx=20, side=LEFT)  # Sol tarafa hizalan�yor ve bo�luk b�rak�l�yor

    # �kinci buton pencereye yerle�tiriliyor
    b2.pack(pady=20, padx=20, side=RIGHT)  # Sa� tarafa hizalan�yor ve bo�luk b�rak�l�yor
    b2.place(x=50, y=10, width=100, height=30)  # Ayr�ca belirli koordinatlara yerle�tiriliyor

    # Tkinter ana d�ng�s�n� ba�lat�yoruz
    pencere.mainloop()

# `islem` fonksiyonunu �a��rarak program� ba�lat�yoruz
islem()
