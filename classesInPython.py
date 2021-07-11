# Understanding python class
class Myfamily():
    #Doc string
    """This class initiates names of my siblings as objects in the 'Myfamily'. Enjoy it"""
    def __init__(self, name, age, status, number):
        self.fullname = name
        self.age = age
        self.merital_status = status
        self.born_number = number
    def intro(self):
        print(f"My name is {self.fullname}. I'm {self.age} yrs. I'm {self.merital_status}. Born number {self.born_number} in our family")


firstborn = Myfamily("Charlton Andaloti abisai",37,"married","One")

secondborn = Myfamily("Frinda Mutanda Abisai",35,"married","Two")

thirdborn = Myfamily("Duncan Lichuma Abisai",32,"married","Three")

fourthborn = Myfamily("Robert Musungu Abisai",30,"Single","Four")

fifthborn = Myfamily("Brendah Akhutu Abisai",28,"Married","Fifth")


print(firstborn.fullname)

print(f"{firstborn.fullname}\n") 

print(f"{firstborn.intro()}\n")

print(f"{fourthborn.fullname} is {fourthborn.merital_status}")

