## s = 1 - 1/3! + 1/5! - 1/7! + ....... n terms

def fact(n):
    fact_total = 1
    
    for i in range(1,n+1):
        fact_total *= i
        
    return fact_total

n = int(input())
s = 0

for i in range(1,n+1):
    if i % 2 != 0:
        s -= 1/fact(n)
    else:
        s += 1/fact(n)
        
print(s)
     
