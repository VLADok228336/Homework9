from random import*
def matrix():
    k = []
    for i in range(10):
        l = []
        for f in range(10):
            l.append(0)
        k.append(l)
    for i in range(10):
        k[randint(0, 9)][randint(0, 9)] = 1
    return k

matr = matrix()
for i in matr:
    print(i)
def turn(x, y):
    sum = 0
    if matr[x][y] == 0:
        
        try:
            sum+=matr[x-1][y]
        except:
            aaaaa=1
        try:
            sum+=matr[x+1][y]
        except:
            aaaaa=1
        try:
            sum+=matr[x][y-1]
        except:
            aaaaa=1
        try:
            sum+=matr[x][y+1]
        except:
            aaaaa=1
        try:
            sum+=matr[x-1][y-1]
        except:
            aaaaa=1
        try:
            sum+=matr[x+1][y+1]
        except:
            aaaaa=1
        print(sum)
    return matr[x][y] == 1
def main():
    
    isGameOver = False
    while not isGameOver:
        r = input("Enter coords ").split(", ")
        isGameOver = turn(int(r[0]), int(r[1]))
    print("Kaboom")
main()