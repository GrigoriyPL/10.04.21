print ('Программа запущена')
ocenki = input()
ocenki = ocenki.split()
kolvo = 0
vsego = 0
for i in ocenki:
    kolvo += 1
    vsego += int(i)
print (vsego/kolvo)