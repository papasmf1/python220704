# DemoFormat.py 

url = "http://ycampus.com/?page=" + str(1) 
print(url)

for i in range(1,6):
    print(i,"*",i,i*i)

print("---정렬 방식 지정---")
for i in range(1,6):
    print(i,"*",i, str(i*i).rjust(3))

print("---정렬 방식 지정---")
for i in range(1,6):
    print(i,"*",i, str(i*i).zfill(3))


