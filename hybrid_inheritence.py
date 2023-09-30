class A:
    def display(self):
        print('display from calss A')
    
class B(A):
    def display(Self):
        print('display from class B')

class C:
    def show(self):
        print('hi from C class')
class D(B,C):
    def display(self):
        print('Display from class D')
        

d1=D()
print(D.mro())