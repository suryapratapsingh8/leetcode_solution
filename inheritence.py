class human:
    def __init__(self,specialze) -> None:
        self.eyes=2
        self.ears=2
        self.specializ=specialze
    def eat(self):
        print('Ican eat')
    def work(self):
        print('I can work')

class Male(human):
    '''def work(self):            #method overriding
        print('I can code')'''
    def __init__(self,Name) -> None:
        self.name=Name 
        super().__init__('python')
    def abc(self):
        super().work()
        print('I can code')

male_1=Male('surya')

male_1.eat()
male_1.abc()
print(male_1.eyes,male_1.name,male_1.specializ)


