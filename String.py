name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")

print(f"Isminizin uzunlugu {len(name)} dir . " )

index = name.find(" ")
print(f"{index}. indexte bosluk vardir . ")

name = name.capitalize() # baþ harfi büyütür
name = name.upper() # Hepsini büyütür
name = name.lower() # Hepsini küçültür

print(name.isdigit())   # Hepsinin sayý olmasýna bakar

print(name.isalpha())   # Boþluk olmayacak , sayý olmayacak sadece harf

result = phone_number.count(" ") # Boþluklarý sayan bir row

phone_number = phone_number.replace("-", " ") # Replace komutu "-" yerine boþluk koyuyor burada
print(phone_number)