# input (갯수, 더하는 회수, 각 숫자당 사용획수)
# 5 8 3 
# 2 4 5 4 6

# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0 

while True :
    for i in range(k):
        if m ==0:
            break
        result +=first
        m -= 1
    if m == 0 :
        break
    result+=second
    m-=1

print(result) # 최종 답안 출력