import random


Words_Bank = ["DEAL","COOL","FOOL","WATER"]
User_Mistakes = 0
x = random.randint(0, len(Words_Bank)-1)
Correct_chars = []
Wrong_chars = []
Word = Words_Bank[x]

#Word = random.choice(Words_Bank)

while User_Mistakes < 6: 
    for i in range(len(Word)):
       if Word[i] in Correct_chars:
            print(Word[i], end=" ")
       else:      
            print("_", end=" ")
    
    if  set(Correct_chars) == set(Word):
        print("YOU WON!")
        break        
    user_guess = input("type a letter: ")
    if len(user_guess) == 1:
        if user_guess.upper() in Word:
            Correct_chars.append(user_guess.upper())

        else:
            Wrong_chars.append(user_guess)
            User_Mistakes +=1
            print("WRONG!")
    else:
        print("just one letter!")
if User_Mistakes == 6:
    print("K.O!")
    