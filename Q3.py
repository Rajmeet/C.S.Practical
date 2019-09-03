def GenerateFactors(n): 
    factors = []
    for i in range(1, (n//2) + 1):
        if n % i == 0:
            factors.append(i)
    factors.append(n) 
    return factors  

def isPrime(n):
    return ((len(GenerateFactors(n))) == 2)

def isPerfect(n):
    return sum(GenerateFactors(n)) == n*2

print(GenerateFactors(12))
print(isPrime(3))
print(isPerfect(6))
