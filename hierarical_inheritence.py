class Human:
    def __init__(self,name,age) -> None:
        self.name=name 
        self.age=age
    def showdetails(self):
        print(f"my name is {self.name} and age is {self.age}")
    def eat(self):
        print('I can eat')


class Male(Human):
    def work (self):
        print('I can Work')

class Boy(Human):

    def dance(self):
        print('I can Dance')

boy_1=Boy('surya',21)
male_1=Male('rahul',22)
boy_1.eat()
male_1.eat()
boy_1.showdetails()
print(Boy.mro())
