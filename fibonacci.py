#write a python program for fibonacci numbers
def fibonacci(n,fibo={}):
    fibo[0]=0
    fibo[1]=1
    for i in range(2,n+1):
        fibo[i]=fibo[i-1]+fibo[i-2]
    return fibo[n]
n=10
res=fibonacci(10)
print(res)
#output
#55
