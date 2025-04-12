
#try - except

# try:
#     print(a / b)
# except:
#     print('Xəta baş verdi')

# print("Salam")

#try - except

# try:
#     a = int(input())
#     b = int(input())
#     print(a / b)
# except ZeroDivisionError:
#     print('0-a bölmək olmaz')
# except ValueError:
#     print("Doğru data daxil edilmədi")

# print("Salam")



# try:
#     a = int(input())
#     b = int(input())
#     print(a / b)
# except (ZeroDivisionError, ValueError):
#     print('Sıfıra bölmə və ya data xətası baş verdi')

# print("Salam")


# try:
#     a = int(input())
#     b = int(input())
#     print(a / b)
# except ZeroDivisionError as e:
#     print(f'Sıfıra bölmə və ya data xətası baş verdi, {e}')

# except ValueError as e:
#     print('Data xətası baş verdi', e)

# print("Salam")


# try:
#     a = int(input())
#     b = int(input())
#     print(a / b)

# except ZeroDivisionError:
#     print('0-a bölmək olmaz')

# except Exception as e:
#     print('Xəta:', e)

# try:
#     a = int(input())
#     b = int(input())
#     print(a / b)

# except:
#     print('Xəta')

# else:
#     print('Uğurla yerinə yetirildi')

# finally:
#     print("İşə düşdü")


# try:
#     a = 5
#     b = 'Salam'
#     print(a + b)
# except TypeError:
#     print('Doğru datalar deyil')


# try:
#     A = [1,2,3,4,5]
#     A[10]
# except IndexError as e: 
#     print('Index doğru deyil', e)

def my_func(a, b):
    if b == 0:
        raise ZeroDivisionError('0-a bölmək olmaz')
    
    return a / b

try:
    my_func(4, 0)
except ZeroDivisionError as e:
    print(e)