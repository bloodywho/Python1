name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")

print(f"Isminizin uzunlugu {len(name)} dir . " )

index = name.find(" ")
print(f"{index}. indexte bosluk vardir . ")

name = name.capitalize() # ba� harfi b�y�t�r
name = name.upper() # Hepsini b�y�t�r
name = name.lower() # Hepsini k���lt�r

print(name.isdigit())   # Hepsinin say� olmas�na bakar

print(name.isalpha())   # Bo�luk olmayacak , say� olmayacak sadece harf

result = phone_number.count(" ") # Bo�luklar� sayan bir row

phone_number = phone_number.replace("-", " ") # Replace komutu "-" yerine bo�luk koyuyor burada
print(phone_number)