class human:
    def __init__(self,heart) -> None:
        print('calling from human class')
        self.eyes=2
        self.nose=1
        self.heart=3
    def eat(self):
        print('I can eat')
    def work(self):
        print('I can work')


class male:
    def __init__(self,name) -> None:
        print('calling from male class')
        self.Name=name
    def flirt(self):
        print('I can flirt')
    def work(self):  
        print('I can code')

class boy(human,male):
    def __init__(self,naam,heart,language) -> None:
        self.language=language

        male.__init__(self,naam)
        human.__init__(self,heart)
    def display(self):
        print(f'hi i am {self.Name}')
    
    

boy_1=boy('Rahul',2,'python')
'''boy_1.flirt()
boy_1.work()
male.work(boy_1)'''
#print(boy_1.language,boy_1.Name)
boy_1.display()
