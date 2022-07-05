#부모 클래스 정의 
class Person:
    #초기화 메서드 
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    #인스턴스 메서드 
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
    def methodA(self):
        pass 
    def methodB(self):
        pass 
    
#자식 클래스 정의(대학생) 
class Student(Person):
    #상속받은 메서드를 재정의(덮어쓰기, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모 클래스의 생성자를 호출 
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속 받은 메서드를 재정의
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "191122")

p.printInfo()
s.printInfo() 


