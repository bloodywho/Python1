# tkinter ve tkinter.messagebox mod�llerini i�e aktar�yoruz
import tkinter
import tkinter.messagebox

# MyGUI adl� bir s�n�f tan�ml�yoruz
class MyGUI:
    # S�n�f�n kurucu metodu
    def __init__(self):
        # Ana pencereyi olu�turuyoruz
        self.pencere = tkinter.Tk()
   
        # Birinci etiket: Kullan�c�ya ho� geldiniz mesaj�
        self.label = tkinter.Label(self.pencere, text="WELCOME!")
        
        # �kinci etiket: Program hakk�nda bilgi
        self.label2 = tkinter.Label(self.pencere, text="This is my GUI program!")
    
        # Birinci buton: T�kland���nda bir i�lev �al��t�r�r ve metni k�rm�z� renklidir
        self.button = tkinter.Button(
            self.pencere,
            text="Click ME!",  # Buton �zerindeki yaz�
            command=MyGUI.islem1,  # T�klan�nca �al��acak olan metod
            fg="red"  # Buton yaz� rengi
        )

        # �kinci buton: Pencereyi kapat�r ve metni mavi renklidir
        self.button1 = tkinter.Button(
            self.pencere,
            text=" QUIT !",  # Buton �zerindeki yaz�
            command=self.pencere.destroy,  # T�klan�nca pencereyi kapat�r
            fg="blue"  # Buton yaz� rengi
        )

        # Etiket ve butonlar� ana pencereye yerle�tiriyoruz
        self.label.pack()  # Birinci etiketi pencereye ekler
        self.label2.pack()  # �kinci etiketi pencereye ekler
        self.button.pack()  # Birinci butonu pencereye ekler
        self.button1.pack()  # �kinci butonu pencereye ekler

        # Tkinter ana d�ng�s�n� ba�lat�yoruz
        tkinter.mainloop()

    # Birinci butonun t�kland���nda �al��t�rd��� metod
    @staticmethod  # Bu metod s�n�fla ili�kilidir ve parametre olarak `self` almaz
    def islem1():
        # Bir bilgi kutusu g�sterir
        tkinter.messagebox.showinfo("Response", "Thanks for clicking Button!")

# MyGUI s�n�f�n�n bir �rne�ini olu�turuyoruz ve GUI'yi ba�lat�yoruz
my_gui = MyGUI()
