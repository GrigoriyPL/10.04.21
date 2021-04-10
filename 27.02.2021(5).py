high = input()
maxn = 0
minn = 10000000000000
while high != 's':
    print(high)
    high = int(high)
    if high < 160 or high > 180:
        break
    if high < minn:
        minn = high
        print('min', minn)
    if high > maxn:
        maxn = high
        print('max', maxn)
    high = input()
