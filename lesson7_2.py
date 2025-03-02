#While dövrü
# count = 0

# while count < 10: # 10 < 10 -> False
#     print(count) #count = 5
#     count += 1 
#     if count == 5:
#         continue

# i = 0

# while i < 5:
#     i += 1
#     print(i)

# Reqemlerin sayi
# a = int(input('Ededi daxil edin: '))
# # a = str(a)
# # print(len(a))
# # a = 1234 # count 1
# # a = 123 # count 2
# # a = 12 #count 3
# # a = 1 #count 4
# # a = 0 #Dovr bitir
# count = 0
# while a != 0:
#     count += 1 # Count 4, a:1
#     a = a // 10 # Count 4, a:0
#     print(f'Count {count}, a:{a}') #Count 3, a:1
# print(count)    
    
# a = int(input('Ededi daxil edin:'))

# while a < 0:
#     print('Menfi eded daxil etdiniz!')
#     a = int(input('Yeniden daxil edin:'))

# print("Musbet ve ya 0 daxil etdiniz")

#                                    a  b
#Fiboacci ededleri -> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# a = 0
# b = 1
# print(a)
# a = 0
# b = 1
# n = int(input('Serheddi daxil edin: '))

# while a < n:
#     print(f'a:{a}|b:{b}')
#     a, b = b, a + b

# Reqemlerin cemi
# a = int(input('Ededi daxil edin: '))
# # a = 1234 # cem 4
# # a = 123 # cem 7
# # a = 12 #cem 9
# # a = 1 #cem 10
# # a = 0 #Dovr bitir
# count = 0

# while a != 0:
#     count += 1 # Count 4, a:1
#     a = a // 10 # Count 4, a:0
#     print(f'Count {count}, a:{a}') #Count 3, a:1

#Qonşu olub-olmaması

# n = 122345
# a = n % 10

# n = 12234
# a = 5
# a == n % 10 # 4
# a = n % 10
# n = n // 10

# n = 1223
# a = 4
# a == n % 10 # 3
# a = n % 10
# n = n // 10

# n = 122
# a = 3
# a == n % 10 # 2
# a = n % 10
# n = n // 10

# n = 12
# a = 2
# a == n % 10 # 2
# --------------break
# a = n % 10
# n = n // 10

n = int(input("Ededi daxil edin: ")) # 12345
flag = False
a = n % 10 # 5

while n > 0:
    n = n // 10 # 0
    print('N',n,'a',a)
    if a == n % 10: # 1 == 0
        flag = True
        break
    a = n % 10 # a = 1

if flag == True:
    print('Qonsu ededlerden beraber olan var')
    
else:
    print('Qonsu ededlerden beraber olan yoxdur')