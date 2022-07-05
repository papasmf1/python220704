# class1.py 
#1)클래스 형식을 정의
class Person:
    #초기화 메서드(생성자)
    def __init__(self):
        #인스턴스 멤버 변수
        self.name = "default name"
    #인스턴스 메서드 
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p1.print() 

