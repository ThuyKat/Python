def fun(n):
    if n == 0:
        return
    fun(n-1)
    print(n)
fun (5)
def fun_reverse(n):
    if n ==0:
        return
    print(n)
    fun_reverse(n-1)
fun_reverse(5)
