message = 'Hello There. My name is Sadık Turan'.split()
print(message[0])

my_list= [1,2,3]
my_list=['bir',2,True,5.6]
print(my_list)

list = ['one','two','there']
list2 = ['four','five','six']
numbers = list + list2
print(numbers)
print(len(numbers))
print(numbers[2])

userA = ['Sadık',36]
userB= ['Çınar',2]
users = [userA , userB]
print(users[1][1])

#'Bmw, Mercedes, Opel, Mazda' elemanlarına sahip bir liste oluşturun
arabalar = ['Bmw','Mercedes','Opel','Mazda']

#Liste kaç elemanlıdır
result = len(arabalar)
print(result)

#Listenin ilk ve son elemanı nedir
print(arabalar[0])
print(arabalar[len(arabalar)-1])

#Mazda değerini Toyota ile değiştirin
arabalar[3] = 'Toyota'
print(arabalar)

#Mercedes listenin bir elemanı mıdır?
result = 'Mercedes' in arabalar
print(result)

#Listenin son 2 elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin
arabalar[-2:] = ['Toyota', 'Renault']
print(arabalar)

#Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin
arabalar = arabalar + ['Audi','Nissan']
print(arabalar)

#Listenin son elemanını silin
del arabalar[len(arabalar)-1]
print(arabalar)

#Liste elemanlarını tersten yazdırın
print(arabalar[::-1])

