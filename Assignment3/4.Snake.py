n = int(input("How long do u want your sanke? "))
for i in range(n):
    if i%2==0:
        print("*", end="")
    else:
        print("#", end="") 
