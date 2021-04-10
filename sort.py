print ('Программа работает . . .')
a = [0, 5, 6, 2, 3, 7, 1, 9, 8, 4]
for b in range (len(a)):
    for i in range (len(a)-1):
        if a[i] > a[i+1]:
            vspom = a[i]
            a[i] = a[i+1]
            a[i+1] = vspom
print(a)