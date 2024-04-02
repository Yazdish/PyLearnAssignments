Length = int(input("please enter the length of your list: "))
Array =[]
for i in range(Length):
    x = int(input("enter numper: "))
    Array.append(x)
if Array != sorted(Array):
    print("your list is NOT sorted.")
else:
    print("your list is sorted")
