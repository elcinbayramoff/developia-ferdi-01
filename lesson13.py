#1.Verilmiş massivin elementlərini formatlayaraq ekrana çıxarın.

# A = [1, 5, 7, 9, 2, 4]
# #A[2] = 7

# for i in range(len(A)):
#     print(f'A[{i}] = {A[i]}')

#2. Massiv elementlərinin istifadəçi tərəfindən daxil edilməsi ilə bağlı proqram yazın. 
# Nəticədə yaranmış listi ekrana çıxarın.

# length = int(input('Listing uzunluğunu daxil edin: '))

# A = []
# for i in range(length):
#     a = int(input(f'A[{i}] = '))
#     A.append(a)

# print(A)

#4.
# A = [1,2,5,3,4,5,6,9]
# flag = False
# for i in range(len(A)):
    
#     for j in range(i+1,len(A) ):
#         if A[i] == A[j]:
#             flag=True

# if flag:
#     print('Eyni tapıldı')

# else:
#     print('Eyni tapılmadı')

#9.
# A = [1, -3, 4, 2, -5, -6]
# menfi = []
# musbet = []

# for i in A:
#     if i  < 0:
#         menfi.append(i)
#     else:
#         musbet.append(i)

# umumi = menfi + musbet
# print(umumi)
#10.

# A = [1, -3, -4, 2, -5, -6]

# for i in A:
#     if i % 2 == 0 and i < 0:
#         print(i)