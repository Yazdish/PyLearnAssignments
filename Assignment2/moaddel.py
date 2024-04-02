
Sum = 0
Reps = 0
Mean = 0

while True:
        user_input = input("enter ur score or write exit to end the process :")
        if user_input == "exit":
                print("ur Mean is :", Mean)
                break
        else:
                user_input = float(user_input)
                Sum = Sum + user_input
                Reps = Reps + 1
                Mean = Sum / Reps
                