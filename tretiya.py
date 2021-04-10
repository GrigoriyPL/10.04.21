kolvo = int(input())
mass = []
for i in range (kolvo):
    chislo = int(input())
    mass.append(chislo)
for i in range (kolvo - 1):
    print (mass[i] + mass[i+1])
