def fun_1(n):
    if n == 0:
        return
    print(n)
    fun_1(n-1)
    print(n)
fun_1(3)

def fun_2(n):
    if n == 0:
        return
    fun_2(n-1)
    print(n)
    fun_2(n-1)

fun_2(3)

def fun_3(n):
    if n <=1:
        return 0
    else:
        return 1 + fun_3(n//2)
print(fun_3(16))