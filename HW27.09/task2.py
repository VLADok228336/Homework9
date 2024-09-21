from random import*
def matrix():
    k = []
    for i in range(5):
        l = []
        for f in range(5):
            l.append(randint(10, 99))
        k.append(l)
    

    maximum = 0
    minimum = 100
    for i in k:
        if max(i)>maximum:
            maximum = max(i)
        if min(i)<minimum:
            minimum = min(i)
    return minimum, maximum
print(matrix())
        