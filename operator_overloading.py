class Complex_num:
    def __init__(self,r,i) -> None:
        self.real=r  
        self.imaginary=i

    def __add__(self,other):
           return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"

c1=Complex_num(1,2)
c2=Complex_num(4,5)
print(c1+c2)