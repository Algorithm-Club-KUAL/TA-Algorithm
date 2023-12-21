up1, down1 = map(int, input().split())
up2, down2 = map(int, input().split())
def gcd1(a,b):
    reala = a
    realb = b
    while b:
        a = a % b
        a,b = b,a
    return (reala * realb // a)
def gcd2(a,b):
    while b:
        a = a % b
        a,b = b,a
    return (a)
Min = gcd1(down1, down2)
mut1 = Min // down1
mut2 = Min // down2
#print(Min, mut1, mut2) #35 5 7

up3 = up1 * mut1 + up2 * mut2
down3 = Min

Min2 = gcd2(up3, down3)
print(up3//Min2 , down3//Min2)