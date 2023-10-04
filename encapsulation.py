class student:
    def __init__(self,name,roll_no,age) -> None:
        self.name=name 
        self._rollno=roll_no #PRIVATE ACCESS MODIFIER
        #self._rollno=roll_no #PROTECTED ACCESS MODIFIER
        self.__age=age

    def get_age(self):
        return self.__age 
    
    def set_age(self,new_age):
        self.__age=new_age

''' def __display(self):
        print("Calling from student class")

    def displayprivate(self):
        self.__display()

class Branch(student):
    def show(self):
        print(f"my roll no is {self._rollno}")
        

b1=Branch('rahul',22,21)
print(b1.name)
b1.show()
print(b1._student__age)
b1._student__display()'''

s1=student('Rahul',30,23)
s1.set_age(24)
print(s1.get_age())