import random
while True:
    print("[0] = Exit")
    print("[1] = Roll")
    user_input = int(input('Roll?!'))
    if user_input == 1:
        Dice = random.randint(1,6)
        print("Dice Value: ", Dice)
        if Dice == 6 :
            print("JackPot! \n enter [1] to Roll")
    elif user_input == 0:
        break
    else: 
        print("invalid operation *_* ")