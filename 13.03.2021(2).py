n = int(input())
m = int(input())
sym = input()
for i in range(1, n+1):
    if i == 1 or i == n:
        print(sym * n)
    else:
        for i in range (1, n-1):
            print(sym, ' '*(n-2), sym,sep='')
            break

