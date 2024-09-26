from random import*
used = []
def matrix():
    k = []
    for i in range(7):
        l = []
        for f in range(7):
            l.append(randint(0, 25))
        k.append(l)
    return k


    
def turn(k, a, b):
    global used
    return k[a][b]
def game(d, k):
    p = [1, 2, 3]
    sum = 0
    print(f"Player {d}'s turn")
    for i in p:
        r = input().split(", ")
        
        if f"{r[0]}, {r[1]}" in used:
            p.append(1)
            print("U entered recently used coords")
            continue
        else:
            used.append(f"{r[0]}, {r[1]}")
            sum+=turn(k, int(r[0])-1, int(r[1])-1)
    return sum
def main():

    k = matrix()
    print("New game started")
    sum1=0
    sum2=0
    player = 1
    for i in range(6):
        if player==1:
            sum1+=game(player, k)
            player=2
        else:
            sum2+=game(player, k)
            player = 1
    if sum1>sum2:
        print("player 1 wins")
    else:
        print("player 2 wins")
main()  
        
