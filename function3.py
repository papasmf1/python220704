# function3.py
#교집합 함수
def intersect(prelist, postlist):
    #교집합 문자를 담을 지역변수 리스트 
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #특정 글자가 postlist에 있고 그러면서 글자가 아직 result에 없는 경우 
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출 
print(intersect("HAM","SPAM"))

#지역변수와 전역변수
x = 1 
def func1(a):
    return a+x 

#호출
print(func1(1))

def func2(a):
    x = 2 
    return a+x 

#호출
print(func2(1))

print("---불변형식---")
a = 1.2 
print(id(a))
a = 2.3 
print(id(a))

print("---가변형식---")
lst = [1,2,3]
print(id(list))
lst.append(4)
print(id(list))

#객체는 참조를 통해 복사(입력+출력)
wordlist = ["J","A","M"]

#함수 정의
def change(x):
    #내부에서 객체의 복사본 생성(Deep Copy)
    x1 = x[:]
    x1[0] = "H"
    print("내부:", x1)

#호출
change(wordlist)
print("함수 호출후:", wordlist)
