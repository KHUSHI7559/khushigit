import random

i = 0
j = 0
while i < 100 or j < 100:
    b = int(input("Enter a number of Dice: "))
    c = random.randint(1, 6)
    print("The winning number is:", c)

    if b == c:
        print("You have Won")
        i = i + 1
        print("Number of wins=", i)
        print("Number of loss=", j)
    elif b != c and b <= 6:
        j += 1
        print("You have Lost")
        print("Number of wins", i)
        print("Number of Loss=", j)
    else:
        print("Error")
        print("Number of wins=", i)
        print("Number of loss=", j)