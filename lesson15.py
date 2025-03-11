#Ən böyük dəyərə malik açar söz

A = {
    'qelem1':80,
    'qelem2':20,
    'qelem3':10,
    'qelem4':15,
    'qelem5':10,
}
acar_soz = '' 
deyer = 0

for key, value in A.items():
    if value > deyer:
        acar_soz = key
        deyer = value

print(acar_soz, deyer)
