# DemoRE.py 
import re 

#print(dir(re))
#특정한 규칙이 있는지?
result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

#match함수
result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())


