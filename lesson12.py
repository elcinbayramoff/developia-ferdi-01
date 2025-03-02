#Short creation of the lists

# A = []
# for i in range(1,11):
#     A.append(i)

# print(A)


# A = [i for i in range(1,11)]
# print(A)

# A = ['hello','hi','nice']

# B = []

# for i in A:
#     B.append(i.capitalize())


# B = [i.capitalize() for i in A]

# print(B)


# A = [1, 3, 4, 6, 8, 5,  2, 9]
# B = []

# for i in A:
#     if i % 2 == 1:
#         B.append(i**2)

# print(B)

# B = [i**2 for i in A if i % 2 == 1]


# print(B)

A = ['hello','hi','nice']
"""
{
    'a':4,
    'b':1

}
"""
# repeat = {}

# for word in A:

#     for letter in word:

#         if letter in repeat:
#             repeat[letter] += 1
#         else:
#             repeat[letter] = 1

"""
{'h': 2, 'e': 2, 'l': 2, 'o': 1, 'i': 2, 'n': 1, 'c': 1}

"""
# print(repeat)


# VOENS = [1234, 2345, 3456, 1234, 3456, 1234]
# voen = int(input('Voeni daxil edin: '))

# count = 0
# for i in VOENS:
#     if i == voen:
#         count += 1
# print(count)


# VOENS = [1234, 2345, 3456, 1234, 3456, 1234]

# repeat = {}
# for voen in VOENS:
#     if voen in repeat:
#         repeat[voen] += 1
#     else:
#         repeat[voen] = 1
# print(repeat)

# A = {
#     1:{
#         'company_voen':1234,
#         'total':1000
#     },
#     2:{
#         'company_voen':2345,
#         'total':1000
#     },
#     3:{
#         'company_voen':1234,
#         'total':1000
#     },
#     4:{
#         'company_voen':1234,
#         'total':1000
#     },
#     5:{
#         'company_voen':3456,
#         'total':1000
#     },
#     6:{
#         'company_voen':3456,
#         'total':1000
#     },
#     12:{
#         'company_voen':4567,
#         'total':1000
#     },
#     7:{
#         'company_voen':5678,
#         'total':1000
#     },
#     8:{
#         'company_voen':1234,
#         'total':1000
#     },
#     9:{
#         'company_voen':2345,
#         'total':1000
#     },
#     10:{
#         'company_voen':7890,
#         'total':1000
#     },
#     11:{
#         'company_voen':7890,
#         'total':1000
#     },

# }

# a = int(input('Voeni daxil edin: '))
# total = 0
# purchase_id = []
# for key, value in A.items():

#     if value['company_voen'] == a:
#         total += value['total']
#         purchase_id.append(str(key))

# print(f'{a} voenli şirkət ümumi {total} ödəniş edib\nÖdəniş kodlar:{','.join(purchase_id)}')

"""Global scope"""

def finder(word, letter):
    count = 0
    """Enclosed scope"""

    def lower_word(word):
        """Local scope"""
        a=5
        return word.lower()
    
    
    for i in lower_word(word):
        if i == letter:
            count += 1
    
    return count


# soz = input('Sözü daxil edin:')
# herf = input('Hərfi daxil edin:')

# say = finder(soz,herf)
# print(f'{soz} sözündəki {herf} hərfi {say} dəfə təkrarlanıb')


"""
Bu gün Bakıya getdim. Sonra Qubaya getdim. Qubada gün çıxmışdı.

"""
sentence = 'Bu gün Bakıya getdim. Sonra Qubaya getdim. Qubada gün çıxmışdı.'

words_raw = sentence.split()

words = [word.rstrip('.') for word in words_raw]

print(words)