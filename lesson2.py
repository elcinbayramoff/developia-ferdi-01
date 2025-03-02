# a = 11
# print('1-ci: ', a)
# a = a + 2
# a += 2
# # a = a * 2
# a *= 2
# #a = a - 2
# a -= 2
# #a = a / 2
# a /= 2
# #a = a % 2
# a %= 2

# print('2-ci: ', a)

# Formatli xaricetmə
# a = 1234.567
# rounded_a = "{:10.3f}".format(a) # _ _ _ 1234.57 Netice string olur
# print(rounded_a)

#abs() - Modulun tapılması 
# a = abs(-5)
# print(abs(-2.5))

#int() - Tam ədədə çevirmək
# a = "5"
# print(type(a))

# a = int(a)
# print(type(a))

# print(a + 7)


# a = "5.7"
# print(type(a))

# a = float(a)
# print(type(a))

# a = "8"
# a = int(a)
# print(a)

# a = "8.7" # Mumkun deyil
# a = int(a)
# print(a)

# a = 8.7
# a = int(a)
# print(a)

# a = "8 7" # Olmaz
# a = int(a)
# print(a)


# a = "8.7"
# a = float(a)
# print(a)

#round() - Yuvarlaqlaşdırmaq

# a = 123.456456456456
# rounded_a = round(a, 3)
# print(type(rounded_a))
# print(rounded_a)

#min() - Minimum tapilmasi
#max() - Maximum tapilmasi

# minimum_eded = min(4,3,1,6,5,-4,7)
# print(minimum_eded)

#Tapsiriq1. Istifadəçi tərəfindən daxil edilmiş iki ədədin minimumunu ekrana 
#çıxarın.

#pow() - Qüvvətə yüksəltmək
# 5 ^ 2, 5 ** 2 = 25
# a = pow(5, 2)
# print(a)

import math

# #Pi ededi
# pi_ededi = math.pi
# print(math.pi)

# sqrt()

# a = math.sqrt(16)
# print(a)

# a = 16 ** (1/2)
# print(a) # 4.0

# print(math.sin(0))

#floor() - Aşağı yuvarlaqlaşdırmaq

# a = math.floor(3.9)
# print(a)

# ceil() - Yuxarı yuvar...

# a = math.ceil(3.6) # 3 < 3.6 < 4

# a = math.ceil(-3.6) # -3 > -3.6 > -4

# print(a)