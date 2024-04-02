import random
print('Guess Number between 10 & 40\n you have 10 chances ' )

pc_number = random.randint(10,40)
for i in range (10):
    user_number = int(input())
    j = i + 1
    if user_number == pc_number:
        print("You Won! after", j, "guesses.")
        break
    
    elif user_number > pc_number:
        print("Go lower!")

    elif user_number < pc_number:
        print("Go higher!")
    
    else:
        print("You Lost")