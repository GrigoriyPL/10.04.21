num = int(input())
n1 = num // 100 
n2 = num - n1 * 100 
n2 = n2//10
n3 = num-n1*100-n2*10
if n1<n2 and n1<n3 and n2<n3:
    print(n1,n2,n3, sep = '')
elif n1<n2 and n1<n3 and n3<n2 :
    print(n1,n3,n2, sep= '')
elif n2<n3 and n2<n1 and n3<n1:
    print(n2,n3,n1, sep = '')
elif n2<n3 and n2<n1 and n1<n3:
    print(n2,n1,n3, sep = '')
elif n3<n2 and n3<n1 and n1<n2:
    print(n3,n1,n2, sep = '')
elif n3<n2 and n3<n1 and n2<n1:
    print(n3,n2,n1, sep = '')
