class Human:
    def __init__(self,num_hrt) -> None:
        self.num_heart=num_hrt
        self.eyes=2
    def eat(self):
        print('I can Eat')
    def work(self):
        print('I can work')
    

class Male(Human):
    def __init__(self, name) -> None:
        self.name=name
        super().__init__(1)
        
    def sleep(self):
        print('I can sleep')
    def work(self):
        super().work()
        print('I can Code')


class Boy(Male):
    pass 

boy_1=Boy('rahul')
boy_1.eat()
boy_1.work()
print(boy_1.name)
print(boy_1.eyes)
print(boy_1.num_heart)
print(Boy.mro())