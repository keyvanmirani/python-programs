import math
k = int(input())
def phi (n):
    divs = []
    for i in range(2, n):
        if math.gcd(i , n) == 1:
            divs.append(i)
    return divs

def LCMofArray(a):
    lcm = a[0]
    for i in range(1,len(a)):
        lcm = lcm*a[i]//math.gcd(lcm, a[i])
    return lcm
print (LCMofArray(phi(k)))