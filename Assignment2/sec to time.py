Sec = int(input('enter seconds'))
Hour = 0
Min = Sec // 60
Sec = Sec % 60
if Min >= 60:
    Hour = Min // 60
    Min  = Min % 60
print (Hour,":",Min,":",Sec)
