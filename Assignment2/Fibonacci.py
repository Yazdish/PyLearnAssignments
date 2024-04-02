n=int(input("pls enter ur number: "))
fibo = list()
fibo_1 = 0 
fibo_2 = 1
if n==1:
    fibo.append(0)
else:
    fibo.append(0)
    fibo.append(1)    
    for i in range(2, n):
        fibo_3 = fibo_1+fibo_2
        fibo.append(fibo_3)
        fibo_1=fibo_2
        fibo_2= fibo_3
print(*fibo , sep=(", "))    