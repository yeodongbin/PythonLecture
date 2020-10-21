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


