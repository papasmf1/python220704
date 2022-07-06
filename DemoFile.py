# DemoFile.py 
#파일 쓰기 
f = open("c:\\work\\demo.txt", "wt")
f.write("첫번째\n두번째\n세번째라인\n")
f.close()

print("c:/work/test.txt")
#raw string notation(날것 그대로 가공안함) C#(@)
print(r"c:\work\newfile.txt")
