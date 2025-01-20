# tkinter ve tkinter.messagebox mod�llerini i�e aktar�yoruz.
import tkinter
import tkinter.messagebox

# Bir s�n�f olu�turuyoruz, bu s�n�f t�m aray�z bile�enlerini ve i�levleri i�erir.
class MyGUI:

    # S�n�f�n kurucu metodu
    def __init__(self):
        # Ana pencereyi olu�turuyoruz
        self.pencere = tkinter.Tk()
        
        # �st ve alt �er�eveleri olu�turuyoruz.
        # �er�eveler, bile�enleri d�zenlemek i�in kullan�l�r.
        self.top_frame = tkinter.Frame(self.pencere)
        self.bottom_frame = tkinter.Frame(self.pencere)
        
        # Kullan�c�ya mesaj g�steren bir etiket (Label) ekliyoruz.
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text="Enter a distance in kilometers : "  )

        # Kullan�c�n�n kilometre de�eri girece�i bir giri� kutusu (Entry) olu�turuyoruz.
        self.kilo_entry = tkinter.Entry(self.top_frame, width=20)

        # Etiket ve giri� kutusunu �st �er�evenin i�ine yerle�tiriyoruz.
        # `side="left"` ile bile�enleri solda hizal�yoruz.
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        # "Convert" butonunu olu�turuyoruz ve t�klan�nca `convert` fonksiyonunu �a��rmas�n� sa�l�yoruz.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text="Convert ",
                                          command=self.convert)

        # "Quit" butonunu olu�turuyoruz ve t�klan�nca pencereyi kapat�yoruz.
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.pencere.destroy)

        # Butonlar� alt �er�eveye ekliyoruz.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # �er�eveleri ana pencerenin i�ine yerle�tiriyoruz.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Uygulaman�n �al��mas�n� sa�layan d�ng�y� ba�lat�yoruz.
        tkinter.mainloop()

    # Kilometreyi mile �eviren fonksiyon
    def convert(self):
        try:
            # Giri� kutusundan de�eri al�yoruz ve float'a d�n��t�r�yoruz.
            kilo = float(self.kilo_entry.get())
            
            # Kilometreden mile d�n���m yap�yoruz.
            miles = kilo * 0.6214

            # Sonucu bir bilgi mesaj� kutusunda g�steriyoruz.
            tkinter.messagebox.showinfo(
                'Results',
                f'{kilo} kilometers is equal to {miles} miles.')
        except ValueError:
            # E�er kullan�c� ge�ersiz bir de�er girerse, hata mesaj� g�steriyoruz.
            tkinter.messagebox.showerror('Error', 'Please enter a valid number.')

# S�n�f�n bir �rne�ini olu�turuyoruz, bu da GUI'yi ba�lat�yor.
my_gui = MyGUI()
