from random import*
def matrix():
    k = []
    for i in range(5):
        l = []
        for f in range(5):
            l.append(randint(-20, 20))
        k.append(l)
    sum1 = 0
    sum2 = 0
    for i in range(0, 5):
        sum1+=k[i][i]
    for i in range(4, 0, -1):
        sum2+=k[i][i]
    return sum1, sum2
# print(matrix())

