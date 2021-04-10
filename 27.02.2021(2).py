n=int(input())
i=0
x='x'
d=0
for i in range(0,n+1):
    i+=1
    if i!=n:
        d+=1
        print(' '*d,x*d)
    else:
        i=0
