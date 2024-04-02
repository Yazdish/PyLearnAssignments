import random
print("welcome to this GAME")
user_score = 0
pc_score = 0

r = int(input("Chan Tayi!?"))

for i in range (100):        
    user_choice = input("rock? paper? scissors? ")
    if user_choice == "rock":
        user_choice = "rock"
    elif user_choice == "paper":
        user_choice = "paper"
    elif user_choice == "scissors":
        user_choice = "scissors"

    x = random.randint(1, 3)
    if x == 1:
        pc_choice = "rock"
    elif x == 2:
        pc_choice = "paper"
    elif x == 3:
        pc_choice = "scissors"

    print("\npc:", pc_choice, " you: ", user_choice)

    if pc_choice == "rock" and user_choice == "paper":
        user_score = user_score + 1
    elif pc_choice =="paper" and user_choice == "scissors":
        user_score = user_score + 1
    elif pc_choice == "scissors" and user_choice == "rock":
        user_score = user_score + 1
    elif user_choice == "rock" and pc_choice == "paper":
        pc_score = pc_score + 1
    elif user_choice == "paper" and pc_choice == "scissors":
        pc_score = pc_score + 1
    elif user_choice == "scissors" and pc_choice == "rock":
        pc_score = pc_score + 1
    else : print("Draw")
    print("pc: ", pc_score,"   u: ", user_score)
    if pc_score == r:
            print("You Lost")
            break
    elif user_score == r:
            print("You Won")
            break