class Instructor:
    pass 
    def __init__(self,name,address):
        self.y=name
        self.adrs=address
        self.follower=0    #default value for all attribute
        

    def display(self,sub_name):
        print(f"hello {self.y} and i am learning {sub_name}")
    def update_follower(self):
        self.follower+=1

Instructor_1=Instructor('payal','delhi')


Instructor_2=Instructor('surya','gkp')
print(Instructor_1.y,Instructor_1.adrs)

Instructor_2.display('Python')
Instructor_2.update_follower()
print(Instructor_2.follower)
Instructor_1.update_follower()
print(Instructor_1.follower)