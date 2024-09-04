#Problem:
def fibonacci1(n):
    if n<=1:
        return n
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)
    
for i in range(10):
    print(f"{fibonacci1(i)}",end=" ")