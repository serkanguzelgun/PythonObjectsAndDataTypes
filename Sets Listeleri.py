fruits = {'orange', 'apple','banana'}
print(fruits)
#indexlenemez print(fruits[0])

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape','apple'])
#var olan eleman tekrar eklenemez
fruits.remove('mango') #elemanı siler
fruits.discard('apple') #elemanı siler
print(fruits)
fruits.pop() #normalde son elemanı siler fakat burada index olmadığı için kafadan bir eleman siler
print(fruits)
fruits.clear() #tüm elemanları siler
print(fruits)

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList))
#tekrarlanan öğeleri siler