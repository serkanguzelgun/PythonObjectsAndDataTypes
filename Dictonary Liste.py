#key - value
sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

print(plakalar[sehirler.index('kocaeli')])

#plakalar ={ 'key' , 'value'}
plakalar = {'kocaeli' :41 , 'istanbul':34}
print(plakalar['kocaeli'])
plakalar['ankara'] = 6
print(plakalar)

users = {'sadikturan' : { 'age' : 36,
                          'email':'sadik@gmail.com' ,
                          'address': 'kocaeli',
                          'phone': '1231321'
                          },
         'cinarturan': {'age' : 2,
                          'email':'cinar@gmail.com' ,
                          'address': 'kocaeli',
                          'phone': '1231321'
                          }
         }
print(users['cinarturan']['age'])
print(users['cinarturan']['phone'])

ogrenciler = {}
number = input('ögrenci no: ')
name = input('öğrenci adı: ')
surname = input('öğrenci soyad: ')
phone = input('öğrenci telefon: ')

#tek bir tane eklenir
'''ogrenciler[number] = { 'ad' : name,
                       'soyad' : surname,
                       'telefon' : phone
}
print(ogrenciler)'''

#birden fazla eklenir
ogrenciler.update({
    number: {
        'ad' : name,
        'soyad': surname,
        'telefon': phone
    }
})
print(ogrenciler)
print('*'*50)
ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)
print(f'Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}')