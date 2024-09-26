from random import*
def matrix():
    k = []
    for i in range(3):
        l = []
        for f in range(4):
            l.append(randint(0, 9))
        k.append(l)



    summa = 0
    for i in k:
        if sum(i)>summa:
            summa = sum(i)
    return summa
# print(matrix())