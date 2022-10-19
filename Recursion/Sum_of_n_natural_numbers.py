# Sum of n natural numbers using recursion

def sum(n):
    if n<1:
        return 0
    else:
        return n+sum(n-1)

num=int(input('enter a number: '))
print(sum(num))
