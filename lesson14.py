# from my_module import say_hello
# import my_module as mm

# mm.say_hello()

"""
random
randint
choice
choices
uniform
shuffle
"""
# from random import randint
# from my_module import randint
# import random
# import my_module

# random.randint

# my_module.randint

# #random
# print(random.random())

#randint
# print(random.randint(1,5))

#uniform
# print(random.uniform(1,5))

# Shuffle
# A = [1,2,3,4,5,6]
# print(random.shuffle(A))
# print(A)



# # Choice
# A = [1,2,3,4,5,6]
# print(random.choice(A))
# print(A)


# Choice
# A = [1,2,3,4,5,6]
# print(random.choices(A, k=3))
# print(A)

import random

zerler = {
    1:
    """
     -----
    |  *  |
     -----
    """,
    2:
    """
     -----
    | *  *|
     -----
    """
}



def zer():
    A = []
    zer1 = random.randint(1, 2)
    zer1 = zerler[zer1]

    zer2 = random.randint(1, 2)
    zer2 = zerler[zer2]
    return [zer1, zer2]

zer_goruntu = zer()
print(zer_goruntu[0])
print(zer_goruntu[1])



"""
*
**
***
****
"""