#finding the nth number in fibonacci series

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input('Enter the position for fibonacci series: ')) 
print(fibonacci(n))
