import random

def dice():
    return random.randint(1,6)

point1 = 0
point2 = 0
pointc = 0
roundpoint = 0

def Player1():
    global point1
    global roundpoint
    if point1 >= 100:
        return print("Player 1 won the Game!")
    else :
        print("Player1's Turn")
        print(f"Player1's Point {point1}")
        dice = random.randint(1,6)
        print(f"dice is {dice}")
        if dice == 1:
            print("no point")
            roundpoint = 0
            print("*"*20)
            if gametype == "f" or gametype == "friend":
                Player2()
            else:
                PlayerC()
        else:
            roundpoint += dice
            print(f"roundpoint : {roundpoint}")
            while point1 < 100:
                print("OK(O)/Continue(C)?")
                choice = input("Your Choice : ").lower()
                if choice == "o" or choice == "ok":
                    point1 += roundpoint
                    roundpoint = 0
                    print(f"Player1's Point {point1}")
                    if point1 >= 100:
                        print("Player 1 won the Game!")
                        break
                    print("*"*20)
                    if gametype == "f" or gametype == "friend":
                        Player2()
                    else:
                        PlayerC()
                    break
                elif choice == "c" or choice == "continue":
                    Player1()
                    break
                else:
                    print("Wrong Character")

def Player2():
    global point2
    global roundpoint
    if point2 >= 100:
        return print("Player 2 won the Game!")
    else :
        print("Player2's Turn")
        print(f"Player2's Point {point2}")
        dice = random.randint(1,6)
        print(f"dice is {dice}")
        if dice == 1:
            roundpoint = 0
            print("no point")
            print("*"*20)
            Player1()
        else:
            roundpoint += dice
            print(f"roundpoint : {roundpoint}")
            while point2 < 100:
                print("OK(O)/Continue(C)?")
                choice = input("Your Choice : ").lower()
                if choice == "o" or choice == "ok":
                    point2 += roundpoint
                    roundpoint = 0
                    print(f"Player2's Point {point2}")
                    if point2 >= 100:
                        print("Player 2 won the Game!")
                        break
                    print("*"*20)
                    Player1()
                    break
                elif choice == "c" or choice == "continue":
                    Player2()
                    break
                else:
                    print("Wrong Character")

def PlayerC():
    global pointc
    global roundpoint
    if pointc >= 100:
        return print("Player 1 won the Game!")
    else :
        print("Computer's Turn")
        print(f"Computer's Point {pointc}")
        dice = random.randint(1,6)
        print(f"dice is {dice}")
        if dice == 1:
            print("no point")
            roundpoint = 0
            print("*"*20)
            Player1()
        else:
            roundpoint += dice
            print(f"roundpoint : {roundpoint}")
            while pointc < 100:
                print("OK(O)/Continue(C)?")
                if (roundpoint>=20) or ((pointc+roundpoint) >= 100):
                    choice = "ok"
                else:
                    choice = "continue"
                print(f"computer's choice is {choice}")
                if choice == "o" or choice == "ok":
                    pointc += roundpoint
                    roundpoint = 0
                    print(f"Computer's Point {pointc}")
                    if pointc >= 100:
                        print("Computer won the Game!")
                        break
                    print("*"*20)
                    Player1()
                    break
                elif choice == "c" or choice == "continue":
                    PlayerC()
                    break
                else:
                    print("Wrong Character")

print("Play dice game vs computer(c) or a friend(f)")
gametype = input().lower().strip()
Player1()


