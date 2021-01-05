#----------------------------------------
#딕셔너리 : 키와 벨류, 키의 중복을 허락 하지 않는
# Key : Value
# dict = {key:value, key2:value2}
 
#생성
member = {"yeo":"12345", "stu_num":"20201018", "stu_name":"yeodongbin"} #json
temp_dict = {}
print(type(member))
print(member)

d = {'one' : 10, 'two' : 20}
print(d['one'])
print(type(d))
print(dir(d))
print(d.values())
print(d.keys())
print(d.items())

l = list(d.items())
print(l[0][1])

jeju = {'banana' : 5000, 'orange': 2000}
#seoul = jeju
seoul = jeju.copy()
jeju['orange'] = 100000
print(seoul)
print(jeju)

#검색 -> value
print(member['stu_num'])

#변경
member['stu_num'] = '20202020'
print(member['stu_num'])

#삭제
del member['yeo']
print(member)

#추가
member['phone_num'] = '0101234567'
print(member)

#내부 함수 확인
print(dir(member))
print()
print(member.items())

print(member.values())
values_list = list(member.values())

print(member.keys())
keys_list = list(member.keys())

print(keys_list)
print(values_list)

#Key : stu_num 존재여부
print("stu_num" in member)

# Cast dict
# list = [1,2,3], list2 = [seoul, inchon, busan]
# 1:seoul, 2:inchon, 3:busan
list = [1,2,3]
list2 = ["seoul", "inchon", "busan"]
dic_place = dict(zip(list, list2))
print(dic_place)


#문제 # 음식 궁합 체크 프로그램 #####
# input  : 음식 이름을 입력하시오. : 떡볶이
# output : 입력한 음식 떡볶이는 어묵과 궁합이 좋습니다.
#       단, 자료구조에 없으면 다시 질문 받습니다.
foods = {'떡볶이':'어묵', 
          '피자':'파스타', 
          '라면':'김치', 
          '치킨':'맥주',
          '삼겹살': '소주', 
          '파전':'막걸리'}

while True:
    food = input("음식이름을 입력하시오 (" + str(list(foods.keys())) + ") : ")
    if food in foods:
        print("입력한 음식 {0}는 {1}과 궁합이 좋습니다.".format(food,foods.get(food)))
        break
    else:
        print("음식이름을 다시 입력하시오.")

