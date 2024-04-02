T = input("enter HH:MM:SS")
time=list(T.split(":"))
H = time[0]
M = time[1]
S = time[2]
seconds = int(H)*3600 + int(M)*60 + int(S)
print("seconds: ", seconds)