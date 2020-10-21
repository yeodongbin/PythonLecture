# r 읽기
# w 덮어 쓰기
# a 추가 쓰기
# x 쓰기 시, 존재하면 에러 발생

import os
print('프로그램 실행')
print(os.getcwd()+'\log.txt')


''' file writing
f = open('C:/Users/Yeo/PythonLecture/log.txt','w')
f.write('hello python')
f.close()
'''

'''file reading
f = open('c:/python/log/log.txt','r')
print('f.read() : { 0 }'.format(f.read()))
f.close()
'''

'''
with open('c:/python/log/log.txt','r') as f:
    print('f.read() : { 0 }'.format(f.read()))
'''
'''
#리스트 -> 파일 쓰기
ts = ['hello\n','python\n','c++\n','java\n']

with open('c:/python/log/log.txt','w') as f:
    for tl in ts:
        f.write(tl)

with open('c:/python/log/log.txt','w') as f:
    f.writelines(ts)

#모든 문자열 읽기
with open('c:/python/log/log.txt','r') as f:
    ls = f.readlines()
    print('type(ls) : {0}'.format(type))

    l = ''
    for l in ls:
        print(l, end='') #end = '' 계행 삭제, print가 개행을 가지고 있음
'''


#문자열 읽기
with open('C:/Users/Yeo/PythonLecture/log.txt','r') as f:
    l = f.readline()
    print('type(l) : {0}'.format(type(l)))

    c = 1
    
    while l != '':
        print(l, end ='')
        print()
        l = f.readline()
        c+= 1

    print('c-1 : {0}'.format(c-1))




############################################################# 파일의 내용을 행(line) 숫자만큼 출력
inFp = None # 입력파일 초기화
inStr = '' # 읽어올 문자열 초기화

inFp = open("C:/data1.txt", "r", encoding="utf-8")
# 변수에 열 파일 내용 저장, "r"은 읽기 모드, 인코딩은 저장한 인코딩과 맞춰줌
# / 슬레시 사용할때는 1개 , \\ 역슬레시 사용할 때는 2개
# "C:\\data1.txt"


inStr=inFp.readline()
print(inStr, end='')
# 변수에 저장한 파일 내용을 한줄씩 입력(read())
inStr=inFp.readline()
print(inStr, end='')

inStr=inFp.readline()
print(inStr, end='')

inFp.close()
# open()으로 열어놓은 파일 닫기

#### 파일에 있는 모든 내용을 출력
inFp = None # 입력파일 초기화
inStr = '' # 읽어올 문자열 초기화

inFp = open("C:/data1.txt", "r", encoding="utf-8")

while True :
    inStr = inFp.readline()
    if inStr == "":
       break;
    print(inStr, end="")
inFp.close()

# Quiz) 메모장에서 읽어 온 각 라인 앞에 번호를 함께 출력


### 한번에 모두 읽어 들이기
inFp = None # 입력파일 초기화
inStr = '' # 읽어올 문자열 초기화

inFp = open("C:/data1.txt", "r", encoding="utf-8")

inStr = inFp.readlines()
print(inStr)
inFp.close()


### 한번에 모두 읽어 들이고 한줄씩 출력
inFp = None # 입력파일 초기화
inList, inStr =[], '' # 읽어올 문자열 초기화

inFp = open("C:/data1.txt", "r", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList :
    print(inStr, end="")
inFp.close()



### 파일 암호화 및 암호 해독

print(ord("민"))
# 문자는 숫자 형태로 컴퓨터에 저장 된다
print(chr(48124))
# 숫자를 문자 형태로 출력하면 사람이 보기 편하다

num1 = ord("민") + 10
print(num1)
print(chr(num1))
# '10' 암호화 키, 더하기 연산을 이용한 암호화

num2 = num1 - 10
print(num2)
print(chr(num2))
# 복호화 되는 과정

########################## 암호화, 복호화 프로그램 작성 ###########
inFp, outFp = None, None
inStr, outStr = '',''
i = 0
secu = 0

secuYN = input("1.암호화  2.복호화 /// 번호를 선택하세요 : ")
inFname = input("입력 파일명을 입력하세요 : ")
outFname = input("출력 파일명을 입력하세요 : ")

if secuYN == "1" :
    secu = 100
elif secuYN == "2" :
    secu = -100

inFp = open("c:/"+inFname, 'r', encoding='utf-8')
outFp = open("c:/"+outFname, 'w', encoding='utf-8')

while True :
    inStr = inFp.readline()
    if not inStr :
        break
	# 읽어들일 문자가 더이상 없으면 반복문 종료
    outStr = ""
    for i in range(0, len(inStr)) :
        ch = inStr[i]
        chNum= ord(ch)
        chNum= chNum + secu
        # 문자 암호화
	ch2 = chr(chNum)
        outStr = outStr + ch2
	# 암호화 한 문자를 저장 

    outFp.write(outStr)

outFp.close()
inFp.close()
print("%s --> %s 변환 완료" % (inFname, outFname))

# Quiz) 출력 파일 명 nomal파일명_cipher.txt


################### 바이너리 파일 ########################
# 그림, 음악 등등등 2진수로만 이뤄져 있는 파일
inFp, outFp = None, None
inStr= ''

inFp = open("c:/Windows/notepad.exe",'rb')
outFp = open("c:/Python/notepad.exe",'wb')
# notepad.exe라는 프로그램을 복사 붙여넣기 함

while True :
    inStr = inFp.read()
    if not inStr :
        break

    outFp.write(inStr)

outFp.close()
inFp.close()
print("정상적으로 바이너리 파일이 복사됐음.")

### 윈도우 창 띄우기
from tkinter import *

window = None
canvas = None
XSIZE, YSIZE = 256,256

window = Tk()
canvas = Canvas(window, height=XSIZE, width=YSIZE)

canvas.pack()
window.mainloop()
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image=paper, state="nomal")

















