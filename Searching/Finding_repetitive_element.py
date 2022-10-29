# finding the repetitive elements

a = [1, 3, 2, 3, 4]

for i in range(0,len(a)):
    if a[i] in a[i+1:]:
        print(a[i])
