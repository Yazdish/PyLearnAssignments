class Time:
    def __init__(self,hh,mm,ss):
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()

    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)

    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.second < 0:
            self.minute -= 1
            self.second += 60

        if self.minute < 0:
            self.hour -= 1
            self.minute += 60 

    def sum(self, t):
        s_new = self.second + t.second
        m_new = self.minute + t.minute
        h_new = self.hour + t.hour
        result = Time(h_new, m_new, s_new)
        return result


    def sub(self, t):
        s_new = self.second - t.second
        m_new = self.minute - t.minute
        h_new = self.hour - t.hour
        result = Time(h_new, m_new, s_new)
        return result

    def sec_to_time(self):
        
        self.minute = self.second // 60
        self.second = self.second % 60
        if self.minute >= 60:
            self.hour = self.minute // 60
            self.minute  = self.minute % 60
        result = Time(self.hour, self.minute, self.second)
        return result

    def time_to_sec(self):
        secs = self.hour*3600 + self.minute * 60 + self.second
        return secs

    def GMT_to_Teh(self):
        tehran_time = self.sum(Time(3, 30,0))
        return tehran_time


t1 = Time(3, 55, 32)
t1.show()

t2 = Time(4, 32, 25)
t2.show()

t3 = t1.sum(t2)
t3.show()

t4 = t3.GMT_to_Teh()
t4.show()

t5 = t4.time_to_sec()
print(t5)

t6 = Time(0,0,t5)
t7 = t6.sec_to_time()
t7.show()
