# n>=0
# Iteration solution
def iteration_factorial(n):
    result = 1
    if n == 0:
        result = 0
    for i in range (1,n+1):
       result = result *i
    return result
print(iteration_factorial(4))

# recursion solution
def recursion_solution(n):
    if n ==0:
        return 0
    if n ==1:
        return
    return n*recursion_solution(n-1)
print(recursion_solution(4))
