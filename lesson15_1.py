"""
a - append, faylın sonuna. Yenisini yaradır
x - faylları yaratmaq üçün
r - faylları oxumaq üçün
w - Fayları yazmaq üçün
"""

# f = open('lessons.txt', 'w')

# f.write('Tarix')

# f.close()

# f = open('leader.txt', 'x')

# f = open('lessons.txt', 'a')
# f.write(' incesenet')
# f.close()

# f = open('lessons.txt')
# data = f.read() # Bütün datanı oxuyur
# print(f.tell())
# f.seek(0)
# data1 = f.read()
# f.close()
# print(data, data1)


# f = open('lessons.txt')
# data = f.readline() # Bir setr

# f.close()
# print(data)

# f = open('lessons.txt')
# data = f.readlines() # Bütün datanı oxuyur
# for line in data:
#     print(line.strip())

# f.close()


# f = open('lessons.txt')
# data = f.read(3) # Bütün datanı oxuyur
# f.close()
# print(data)


# f = open('lessons.txt', 'r+')
# data = f.read()
# print(f.tell())
# f.seek(0)
# f.write('Salam')

# f.close()

f = open('lessons.txt', 'r+')
data = f.read()
print(f.tell())
f.seek(0)
f.write('Salam')

f.close()

f = open('lessons.txt','a')

f.write('Salam')

f.close()

with open('lessons.txt','a') as f:
    f.write('Salam')



