class Complex_Number:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def show(self):
        print(self.real, "+", "i", self.image)

    def sum(self, c):
        new_real = self.real + c.real
        new_image = self.image + c.image
        result = Complex_Number(new_real, new_image)
        return result

    def sub(self, c):
        new_real = self.real - c.real
        new_image = self.image - c.image
        result = Complex_Number(new_real, new_image)
        return result

    def mul(self,c):
        new_real = self.real * c.real - self.image * c.image
        new_image = self.real * c.real + self.image * c.image
        result = Complex_Number(new_real, new_image)
        return result
    
c1 = Complex_Number(3, 5)
c1.show()

c2 = Complex_Number(5, 8)
c2.show()

x = c1.sum(c2)
x.show()

y = c2.sub(c1)
y.show()

z = c1.mul(c2)
z.show()