website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama"

#'course' de kaç karakter bulunmaktadır?
result = len(course)
print(result)

#'website' içinden www karakterlerini alın
result = website[7:10]
print(result)

#'course' içinden ilk 15 ve son 15 karakterlerini alın
result = course[0:15]
print(result)
result = course[-15:]
print(result)

#'course' ifadesindeki karakterleri tersten yazdırın
result = course[::-1]
print(result)


name,surname,age,job = 'Bora', 'Yılmaz', 32, 'mühendis'
#Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazın
#'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
result = "Benim adım " + name+ " "+surname+", Yaşım " +str(age)+ " ve mesleğim " + job
print(result)
result = 'Benim adım {} {}, Yaşım {} ve mesleğim {}.' .format(name,surname,age,job)
print(result)
result = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}."
print(result)


#'Hello world' ifadesindeki w harfini W ile değiştirin
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(s)

#'abc' ifadesini yan yana 3 defa yazdırın
result = 'abc' * 3
print(result)

