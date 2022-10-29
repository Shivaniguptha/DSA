# To Find the element that appears once in an array where every other element appears twice

a = [2, 3, 5, 4, 5, 3, 4]

b=list(set(a))
for i in b:
    a.remove(i)
    if i not in a:
        print(i)
