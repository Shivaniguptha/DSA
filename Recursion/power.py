def power(num,n):
    if n!=0:
        return num*power(num,n-1)
    else:
        return 1

num=int(input('Enter a number: '))
n=int(input('Enter power of that number: '))
print(power(num,n))
