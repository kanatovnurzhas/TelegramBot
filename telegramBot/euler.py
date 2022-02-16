def gcd1(a,b):
    if a%b == 0:
        return [b,0,1]
    else:
        q = (a- (a%b) )/ b
        [d, r, s]=gcd1(b,a-q*b)
        return [d,s,r-q*s]
print(gcd1(7,159))