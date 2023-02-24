# факториал
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

# перестановки без повтора
def P(n):
    return factorial(n)

# сочетания без повтора
def C(n,k):
    return (factorial(n)) / (factorial(k) * factorial(n-k))
    
# размещения без повтора
def A(n,k):
    return (factorial(n) / (factorial(n-k)))
    
    
# перестановки с повтором
def nP(nList = []):
    summ = 0
    factmn = 1
    for x in nList:
        summ += x
        factmn *= factorial(x)
    
    return factorial(summ) / factmn
    
# cочетания с повтором
def nC(n,k):
    return C(n+k-1,k)

# размещения с повтором
def nA(n,k):
    return n**k
