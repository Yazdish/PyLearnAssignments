class Fraction:
    def __init__(self,ss,mm):
        self.s = ss
        self.m = mm

    def sum(self,f):
        result_s = self.s * f.m + self.m * f.s
        result_m = self.m * f.m 
        x = Fraction(result_s, result_m)
        return x


    def mul(self,f):
        result_s = self.s * f.s
        result_m = self.m * f.m
        x = Fraction(result_s, result_m)
        return x 

    def sub(self, other):
        result_s = self.s * other.m - self.m * other.s
        result_m = self.m * other.m
        x = Fraction(result_s, result_m)
        return x

    def div(self, other):
        result_s = other.m * self.s
        result_m = other.s * self.m
        x = Fraction(result_s, result_m)
        return x

    def fraction_to_number(self):
        return self.s / self.m


    def greatest_common_divisor(self):
        Greatest_Common_Divisor = 1
        Divisors1 = []
        Divisors2 = []

        for i in range(1,self.s + 1):
            if (self.s / i).is_integer():
                Divisors1.append(i)
                
        for i in range(1,self.m + 1):
            if (self.m / i).is_integer():
                Divisors2.append(i)
                if i in Divisors1:
                    Greatest_Common_Divisor = i

        return Greatest_Common_Divisor

    def simplify_the_fraction(self):
        GCD = Fraction.greatest_common_divisor(self)
        x = Fraction(self.s / GCD, self.m / GCD)
        return x


    def show(self):
        print(self.s , "/", self.m)

    
a = Fraction(12,8)
a.show()

b = Fraction(17,5)
b.show()

z = a.sum(b)
z.show()

w = b.mul(a)
w.show()

y = w.simplify_the_fraction()
y.show()