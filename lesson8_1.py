#Dictionary

# a = {
#     "name":"Elchin",
#     "age":12,
#     "age":17
#     } #dict
# # print(type(a))
# # print(a)
# print(a)


# a = {
#     1: {
#         "name":"Ali", 
#         "surname":"Aliyev"
#         },
#     2: {
#         "name":"Vali", 
#         "surname":"Valiyev"
#         },
#     3: {
#         "name":"Mahmud", 
#         "surname":"Mahmudov"
#         }
#     }

# print(a[2]["surname"])


#.get() və [  ]


# a = {
#     "name":"Elchin",
#     "age":12,
#     "qelem_rengleri":['black','white','red']
#     } 

# # print(a["surname"])
# # print(a.get("surname"))
# value1 = a.get('qelem_rengleri', []) # []
# value2 = a.get('karandas_rengleri', []) # None

# # 
# # if value:
# #     print(value)
# # else:
# #     print('tapilmadi')
# for i in value2:
#     print(i)

# car = {
#     'brand':'Ford',
#     'engine':2.0,
#     'year':2004,
#     'color':'white'
# }

# keys = car.keys()

# # for key in keys:
# #     print(key)
    
# print("Keys", keys)

# values = car.values()
# print("Values", values)
# car = {
#     'brand':'Ford',
#     'engine':2.0,
#     'year':2004,
#     'color':'white'
# }
# items = car.items()

# for key, value in items: #('engine', 2.0)
    # print("Key",key, "Value", value)
# print("Items", items)
# a, b = (1, 2)
# print(a, b)

# car = {
#     'brand':'Ford',
#     'engine':2.0,
#     'year':2004,
#     'color':'white'
# }
# car.clear()
# car.pop('brand')
# del car
# print(car)




# car = {
#     'brand':'Ford',
#     'engine':2.0,
#     'year':2004,
#     'color':'white'
# }

# for i in car:
#     print(i)
#     print(car[i])
#     print('\n')


# for i in car.keys():
#     print(i)
#     print(car[i])
#     print('\n')
# car = {
#     'brand':'Ford',
#     'engine':2.0,
#     'year':2004,
#     'color':'white'
# }

# for i in car.values():
#     print(i)



# car = {
#     'brand':'Ford',
#     'engine':2.0,
#     'year':2004,
#     'color':'white'
# }

# #Dictlere yeni element elave edilmesi ve deyisilmesi
# car['country'] = 'America'
# car['year'] = 2007

# print(car)


# car = {
#     'brand':'Ford',
#     'engine':2.0,
#     'year':2004,
#     'color':'white'
# }

# car1 = car.copy()

# car['brand'] = 'Mercedes'
# print(car)
# print(car1)

# people = {
#     'Elchin':{
#         'brand':'Ford',
#         'engine':2.0,
#         'year':2004,
#         'color':'white'
#             },
#     'Ali':{
#         'brand':'Mercedes',
#         'engine':1.6,
#         'year':1998,
#         'color':'black'
#             },
#     'Vali':{
#         'brand':'BMW',
#         'engine':2.0,
#         'year':2008,
#         'color':'blue'
#             },
# }

# print(people['Ali']['brand'])

# """
# İç-içə lüğətlərdən istifadə edərək 3 adam üçün ad və
# telefon nömrəsindən ibarət kitabça yaradın.
# """

# kitabca = {
#     1 : {
#         'name':'Elchin',
#         'phone':'0707007070'
#     },
#     2 : {
#         'name':'Ali',
#         'phone':'0505005050'
#     },
#     3 : {
#         'name':'Vali',
#         'phone':'0555555555'
#     }
# }

# phone_numbers = []

# for value in kitabca.values():
#     phone_numbers.append(value['name'])
    
# print(phone_numbers)


practice_dict = { #dictionary
    #Key     #Value
    'name'   :'Elchin', #item
    'surname':'Bayramli', #item
    'address':'Baku' #item
}

#1ci
# soyad = practice_dict['surname']
# print(soyad)
#2ci
# ad = practice_dict.get('name', 'Tapilmadi')
# print(ad)

#.values()

# for key, value in practice_dict.items():
#     if value == 'Elchin':
#         print(key)

# print(practice_dict)

# practice_dict = { #dictionary
#     #Key     #Value
#     'name'   :'Elchin', #item
#     'surname':'Bayramli', #item
#     'address':'Baku' #item
# }

# practice_dict['age'] = 19
# print(practice_dict)


# az_en = {
#     'run':'qacmaq',
#     'high':'yuksek',
#     'rain':'yagis',
#     'school':'mekteb'
# }

# sentence = input('Cumleni daxil edin: ')
# sentence_copy = sentence
# # "run high rain school"
# # "qacmaq yuksek yagis mekteb"
# sentence = sentence.strip() #Evvel ve sondan boşluqları təmizlədi

# words = sentence.split()#Cümləni boşluqlara görə ayıraraq sözlərə böldü.Nəticə list oldu
# #['high', 'run', 'slow', 'higher']

# translated_words = []
# for word in words:
    
#     if word in az_en:
#         translated_words.append(az_en[word])
#     else:
#         translated_words.append(word)

# result = ' '.join(translated_words)
# print('Sentence:',sentence_copy)
# print('Translated:',result)


A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]