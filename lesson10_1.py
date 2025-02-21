#set

a = {1, 'Salam', 1.6}

# for i in a:
#     print(i)

# if 'Sal' in a:
#     print(True)

# a = ['a','b','c']

# if 'ab' in "abc":
#     print(True)

# A = {1,3,5,7}

# # A.add(1200)
# # print(A)

# A.update(('abc','def'))
# print(A)


A = {1,3,5,7}

# A.remove(9)

# A.discard(9)0
# A.pop()
# A.clear()
# print(A)

# A = {
#     1:{'name':'Ali,Vali,Pirvali'}
# }

# # A[1]['name'] # ['Ali','Vali']
# adlar = A[1]['name']
# print(adlar.split(','))

#union
# A = {1,3,5,7}
# B = {3,4,6,8}

# # C = B.union(A)

# C = A | B
# print(C)

#update
# A = {1,3,5,7}
# B = {3,4,6,8}

# # A.update(B)
# A |= B
# print(A)

# #intersection

# A = {1,3,5,7}
# B = {3,4,6,8}

# # C = A.intersection(B)
# C = A & B
# print(C)

#intersection_update

# A = {1,3,5,7}
# B = {3,4,6,8}

# # A.intersection_update(B)
# A &= B
# print(A)


# #symmetric_difference

# A = {1,3,5,7}
# B = {3,4,6,8}

# # C = A.symmetric_difference(B)
# C = A ^ B
# print(C)

#symmetric_difference_update

# A = {1,3,5,7}
# B = {3,4,6,8}

# # A.symmetric_difference_update(B)
# A ^= B
# print(A)

#difference

# A = {1,3,5,7}
# B = {3,4,6,8}

# # C = B.difference(A)
# C = B - A
# print(C)

#difference_update

# A = {1,3,5,7}
# B = {3,4,6,8}

# # B.difference_update(A)
# B -= A
# print(B)