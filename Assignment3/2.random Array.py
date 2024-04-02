import random

n = int(input("Length of Array: "))
Array =[]
while len(Array) != n:
    Rand_num= random.randint(0, 10)
    if Rand_num not in Array:
        Array.append(Rand_num)
print(Array)
