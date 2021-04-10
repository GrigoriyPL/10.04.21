n=int(input())
i=1
d=0
while i<n:
    if i%2==0:
        i+=1
        d+=1
    else:
        i=i*2
        d+=1
print(d)
