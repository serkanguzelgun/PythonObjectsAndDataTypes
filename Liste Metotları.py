numbers = [1,10,5,16,4,9,10]

val=min(numbers)
print(val)

val=max(numbers)
print(val)

#listeye veri ekleme
numbers.append(2)
print(numbers)

# istediğin indekste listeye veri ekleme
numbers.insert(0,99)
print(numbers)

#listeden veri silme
numbers.pop() #son indeksteki eleman silinir
numbers.pop(3)
print(numbers)

#listeden karakteri silme
numbers.remove(1)
print(numbers)

#listeyi küçükten büyüğü sıralama
numbers.sort()
print(numbers)

#listeyi tam tersine çevirme
numbers.reverse()
print(numbers)

#eleman sayısını öğrenme
print(len(numbers))

#elemanın kaç defa yazıldığını gösterme
print(numbers.count(10))

#listeyi sıfırlama
print(numbers.clear())

#listedeki en büyük ve en küçük değer nedir?
'''kucuk= min(numbers)
buyuk= max(numbers)
print(kucuk,buyuk)'''


#kullanıcıdan alacağınız 3 adet marka bilgisini bir listede saklama
markalar = []
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
print(markalar)