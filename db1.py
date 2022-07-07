# db1.py 
import sqlite3

#메모리에서 작업(약간의 약속된 문자열)
con = sqlite3.connect(":memory:")
#커서객체를 리턴
cur = con.cursor()
#데이터를 저장할 테이블 생성(varchar, varchar2, nvarchar, char)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")
#입력 파라메터 처리
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
#다중의 레코드 입력(2차원 배열, 행열데이터)
datalist = (("tom","010-345"), ("dsp","010-333"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)
#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)
    

