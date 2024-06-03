message = "Hello There. My Name is Sadık Turan"
print(message)

#Tüm karakterleri büyük yazan metod
message = message.upper()
print(message)

#Tüm karakterleri küçük yazan metod
message = message.lower()
print(message)

#Her kelimenin baş harfini büyük yazan metod
message = message.title()
print(message)

#İfadenin sadece ilk harfini büyük yazan metod
message = message.capitalize()
print(message)

#Baş ve sondaki boşluk karakterlerini silip yazan metod
message = message.strip()
print(message)

#Tüm karakterleri boşluktan ayırıp küme halinde yazan metod
#Neye göre ayrılmasını istiyorsak parantez içine yazarız
message = message.split()
print(message)

#Ayrılan tüm karakterleri birleştiren metod
#Birleştirirken araya ne koymasını istiyorsak tırnak içine yazarız
message =' '.join(message)
print(message)

#İfadenin içindeki kelimeyi bulup index yani bulunduğu konumu veren metod
index = message.find('sadik')
print(index)

#İfadenin ilk harfini doğrulayan metod
isFound = message.startswith('H')
print(isFound)

#İfadenin son harfini doğrulayan metod
isFound = message.endswith('N')
print(isFound)

#İfadenin içindeki kelimeyi değiştiren metod
message = message.replace('sadik', 'Çınar')
print(message)

#İfadeyi istediğimiz sayıda karaktere tamamlayan metod
message = message.center(50,'*')
print(message)