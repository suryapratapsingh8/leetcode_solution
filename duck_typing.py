class Duck:
    def swim(self):
        print('I can swim')
    def speak(self):
        print('Quack Quack')

class Dog:
    def swim(self):
        print('Dog can swim')

    def speak(self):
        print('woof woof')

def display(duck):
    duck.swim()
    duck.speak()
    print('Info displayed')

d=Duck()
d1=Dog()
display(d1)
display(d)
