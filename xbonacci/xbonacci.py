def Xbonacci(signature, n):
    result = signature[:n]
    sig = len(signature)
    for i in range(n - sig):
        result.append(sum(result[-sig:]))
    return result

print(Xbonacci([1,2,3,4],10))
print(Xbonacci([1,0,0,0,0,0,1],1))