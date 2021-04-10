print ('Программа запущена . . .')
vvod = input()
vvod = vvod.split()

prov = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

c = 0

for i in range (int(vvod[0])):
    chek = input()
    chek = chek.split()

stoim = []
stoim_1 = ()
kolvo = []
kolvo_1 = ()
summ = []
summ_1 = ()

for i in range (int(vvod[0])):
    
    for a in chek:
        while a != '*':
            if a in prov:
                stoim_1 += a
            chek.remove(0)
    stoim += stoim_1
    check.remove(0)
    
    for a in check:
        while a != '=':
            if a in prov:
                kolvo_1 += a
            check.remove(0)
    kolvo += kolvo_1
    check.remove(0)

    for a in chek:
        summ_1 += a
    summ += summ_1

print (int(vvod[1]) - int(sum[summ]))
for i in range (int(vvod[0])):
    if int(stoim[i]) * int(kolvo[i]) != int(summ[i]):
        c += 1
print (c)
