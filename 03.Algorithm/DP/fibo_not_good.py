# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현
# 0 1 1 2 3 5 8

def fibo(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(7))