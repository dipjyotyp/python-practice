import math
from collections import Counter

def prime_factors(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            res.append(int(i))
            n = n / i    
    if n > 2:
        res.append(int(n))
    counter = Counter(res)
    res = ''
    for key, value in counter.items():
        if value > 1:
            res += '(' + str(key) + '**' + str(value) + ')'
        else:
            res += '(' + str(key) + ')'
    
    return res

print(prime_factors(86240))