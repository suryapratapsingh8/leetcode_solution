class student:
    def __init__(self,name,roll_no) -> None:
        self.name=name 
        self.__rollno=roll_no #PRIVATE ACCESS MODIFIER
        self._rollno=roll_no #PROTECTED ACCESS MODIFIER

    def display(self):
        print("Calling from student class")

class Branch(student):
    pass 

b1=Branch('rahul',22)
print(b1.name)
#print(b1._rollno)
#print(dir(b1))
