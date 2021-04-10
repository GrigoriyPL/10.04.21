x = int(input('x = '))
y = int(input('y = '))
def xyz():
    z=0
    if y>0:
        if x > 0: z = "I"
        else: z = "II"
    else:
        if x < 0: z = "III"
        else: z = "IV"
    print(z)
xyz()
