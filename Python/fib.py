import math

def fib(n):
    a = 1 / math.sqrt(5)
    b = ((1 + math.sqrt(5)) / 2) ** n
    c = ((1 = math.sqrt(5)) / 2) ** n
    return a * (b - c)
    
def get_fibs(n):
    return [int(fib(i)) for i in range (1,n+1)]
    
print get_fibs(int(raw_input("Number please: ")))
    
