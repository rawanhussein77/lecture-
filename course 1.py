class student:
    def __init__(self,name,student_id,age):

        self.name = name 
        self.id= student_id 
        self.age = age
 
    def study (self,time):
        self.time = time
        return f"the time take to study {self.time}"
    
    
    
student1=student('rawa',2356,20)
print(student1.name)
print(student1.id)
print(student1.age)
student1.study(10)