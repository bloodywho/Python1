# tkinter ve tkinter.messagebox modüllerini içe aktarýyoruz.
import tkinter
import tkinter.messagebox

# Bir sýnýf oluþturuyoruz, bu sýnýf tüm arayüz bileþenlerini ve iþlevleri içerir.
class MyGUI:

    # Sýnýfýn kurucu metodu
    def __init__(self):
        # Ana pencereyi oluþturuyoruz
        self.pencere = tkinter.Tk()
        
        # Üst ve alt çerçeveleri oluþturuyoruz.
        # Çerçeveler, bileþenleri düzenlemek için kullanýlýr.
        self.top_frame = tkinter.Frame(self.pencere)
        self.bottom_frame = tkinter.Frame(self.pencere)
        
        # Kullanýcýya mesaj gösteren bir etiket (Label) ekliyoruz.
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text="Enter a distance in kilometers : "  )

        # Kullanýcýnýn kilometre deðeri gireceði bir giriþ kutusu (Entry) oluþturuyoruz.
        self.kilo_entry = tkinter.Entry(self.top_frame, width=20)

        # Etiket ve giriþ kutusunu üst çerçevenin içine yerleþtiriyoruz.
        # `side="left"` ile bileþenleri solda hizalýyoruz.
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        # "Convert" butonunu oluþturuyoruz ve týklanýnca `convert` fonksiyonunu çaðýrmasýný saðlýyoruz.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text="Convert ",
                                          command=self.convert)

        # "Quit" butonunu oluþturuyoruz ve týklanýnca pencereyi kapatýyoruz.
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.pencere.destroy)

        # Butonlarý alt çerçeveye ekliyoruz.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Çerçeveleri ana pencerenin içine yerleþtiriyoruz.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Uygulamanýn çalýþmasýný saðlayan döngüyü baþlatýyoruz.
        tkinter.mainloop()

    # Kilometreyi mile çeviren fonksiyon
    def convert(self):
        try:
            # Giriþ kutusundan deðeri alýyoruz ve float'a dönüþtürüyoruz.
            kilo = float(self.kilo_entry.get())
            
            # Kilometreden mile dönüþüm yapýyoruz.
            miles = kilo * 0.6214

            # Sonucu bir bilgi mesajý kutusunda gösteriyoruz.
            tkinter.messagebox.showinfo(
                'Results',
                f'{kilo} kilometers is equal to {miles} miles.')
        except ValueError:
            # Eðer kullanýcý geçersiz bir deðer girerse, hata mesajý gösteriyoruz.
            tkinter.messagebox.showerror('Error', 'Please enter a valid number.')

# Sýnýfýn bir örneðini oluþturuyoruz, bu da GUI'yi baþlatýyor.
my_gui = MyGUI()
