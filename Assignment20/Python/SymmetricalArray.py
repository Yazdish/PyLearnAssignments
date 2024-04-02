

print (" Please enter your array's numbers one by one as inputs, and when you are finished print 'done' as an input ")

array = []

while True :
    user_input = input (" Please enter your input :")
    if user_input == "done" :
        break

    else :
        sentence = int (user_input)
        array.append ( sentence )

print ("Your array is : ")
print ( array )

for i in range (len(array)//2) :
    if array[i] != array[len(array) - 1 - i] :
        print (" This array is NOT SYMMETRIC")
        break

else :
    print (" This array is SYMMETRIC")