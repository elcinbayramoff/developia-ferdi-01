#min_max

# A = [1, 3, 5, 2, 7, 4, 6, 3, 4, 5, 6, ]
# if A:
#     max_eded = A[0]
#     for eded in A:
#         if eded > max_eded:
#             max_eded = eded
    
#     print(max_eded)


# A = [9, 3, 5, 2, 7, 4, 6, 3, 4, 5, 6, ]
# #min_eded = 3
# if A:
#     min_eded = A[0]
#     for eded in A:
#         if eded < min_eded:
#             min_eded = eded
    
#     print(min_eded)


A = [9, 5, 7, 4, 6, 3, 4, 5, 6]
#min_eded = 3
def min_finder(A):
    if A:
        min_eded = A[0]
        min_index = 0
        for i in range(len(A)):
            if A[i] < min_eded:
                min_eded = A[i]
                min_index = i
        
        print(min_eded, min_index)
    else:
        print('Listde eded yoxdur')    
min_finder([3,1,4,5])
min_finder([3,1,4,-1,5])
min_finder([5])

min_finder([])

