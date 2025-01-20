# tkinter ve tkinter.messagebox modüllerini içe aktarýyoruz
import tkinter
import tkinter.messagebox

# MyGUI adlý bir sýnýf tanýmlýyoruz
class MyGUI:
    # Sýnýfýn kurucu metodu
    def __init__(self):
        # Ana pencereyi oluþturuyoruz
        self.pencere = tkinter.Tk()
   
        # Birinci etiket: Kullanýcýya hoþ geldiniz mesajý
        self.label = tkinter.Label(self.pencere, text="WELCOME!")
        
        # Ýkinci etiket: Program hakkýnda bilgi
        self.label2 = tkinter.Label(self.pencere, text="This is my GUI program!")
    
        # Birinci buton: Týklandýðýnda bir iþlev çalýþtýrýr ve metni kýrmýzý renklidir
        self.button = tkinter.Button(
            self.pencere,
            text="Click ME!",  # Buton üzerindeki yazý
            command=MyGUI.islem1,  # Týklanýnca çalýþacak olan metod
            fg="red"  # Buton yazý rengi
        )

        # Ýkinci buton: Pencereyi kapatýr ve metni mavi renklidir
        self.button1 = tkinter.Button(
            self.pencere,
            text=" QUIT !",  # Buton üzerindeki yazý
            command=self.pencere.destroy,  # Týklanýnca pencereyi kapatýr
            fg="blue"  # Buton yazý rengi
        )

        # Etiket ve butonlarý ana pencereye yerleþtiriyoruz
        self.label.pack()  # Birinci etiketi pencereye ekler
        self.label2.pack()  # Ýkinci etiketi pencereye ekler
        self.button.pack()  # Birinci butonu pencereye ekler
        self.button1.pack()  # Ýkinci butonu pencereye ekler

        # Tkinter ana döngüsünü baþlatýyoruz
        tkinter.mainloop()

    # Birinci butonun týklandýðýnda çalýþtýrdýðý metod
    @staticmethod  # Bu metod sýnýfla iliþkilidir ve parametre olarak `self` almaz
    def islem1():
        # Bir bilgi kutusu gösterir
        tkinter.messagebox.showinfo("Response", "Thanks for clicking Button!")

# MyGUI sýnýfýnýn bir örneðini oluþturuyoruz ve GUI'yi baþlatýyoruz
my_gui = MyGUI()
