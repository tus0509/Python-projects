from random import randint

print("ROCK PAPER SCISSORS GAME!")
print()
print()
player = input("Rock (r) Paper(p) Scissors(s) ?")
print("Your input: %s" % (player))
comp = randint(1, 3)
if comp == 1:
    comp1 = 'r'
elif comp == 2:
    comp1 = 'p'
else:
    comp1 = 's'
print("Player vs Computer: %s vs %s" % (player, comp1))

if player == comp1:
    print("DRAW!! :P")

if player != comp1:
    if player == 'r':
        if comp1 == 's':
            print("PLAYER WINS :D")
        elif comp1 == 'p':
            print("COMPUTER WINS :P")

    elif player == 'p':
        if comp1 == 's':
            print("COMPUTER WINS :P")
        elif comp1 == 'r':
            print("PLAYER WINS :D")

    else:
        if comp1 == 'p':
            print("PLAYER WINS :D")

        elif comp1 == 'r':
            print("COMPUTER WINS :P")