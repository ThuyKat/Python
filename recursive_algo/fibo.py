# iteration solution:
def it_fibo(n):
    x = 0
    y = 1
    
    for i in range(n):
        z = x
        x = x + y
        y = z
       
    return x

print(it_fibo(7))

def recu_fibo(n):
    
    if n == 0:
        return 0
    if n == 1:
        return 1   
    if n > 1:
       x = recu_fibo(n-1) + recu_fibo(n-2)
    return x
    

print(recu_fibo(7))



    
