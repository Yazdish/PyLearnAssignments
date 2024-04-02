class person:
    def __init__(self,n,a,h,c,e):
        #properties
        self.name = n
        self.age = a
        self.height = h
        self.city = c
        self.country = "iran"
        self.eye_color = e
        self.spouse = None
    
    #methods

    def sleep(self):
        ...
    
    def marry(self,name):
        self.spouse = name
    
    def study(self):
        ...


my_friend = person("ali",30,175,"mashad","black")
my_sister = person("sara", 25, 168, "tehran","blue")
my_boss = person("mammad", 50, 179, "bozghan","brown")


my_sister.marry("ahmad")

print(my_sister.spouse)
