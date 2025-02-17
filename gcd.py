def gcd(a,b):
    if (a==0):
        return b
    if(b==a):
        return a
    if (b==0):
        return a
    if(a>b):
        return gcd(a-b,b)
    return gcd(a,b-a)
a=98
b=56
if (gcd(a,b)):
    print(f"GCD of {a} and {b} is",gcd(a,b))
else:
    print("not found")
    