n1=int(input("First number: "))
n2=int(input("Second number: "))

if n1>n2:
    u=n1
    n1=n2
    n2=u

for i in range(1,n1+1):
    if n1%i==0 and n2%i==0:
        be_mim_mim=i

print("The Be Mim Mim of your numbers is: ", be_mim_mim)