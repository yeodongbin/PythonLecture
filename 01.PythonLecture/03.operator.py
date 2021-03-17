'''
- 연산자(Operator)와 피연산자(operand)
 + , - , * , / 같은 기호들을 연산자
 연산자에 의해 계산이 되는 숫자들은 피연산자
 “3 + 2” 에서 3과 2는 피연산자, +는 연산자
 연산의 순서는 수학에서 연산 순서와같음
 문자간에도+ 연산이가능함

+ (덧셈 연산자)
- (뺄셈 연산자)
* (곱셈 연산자)
** (거듭제곱 연산자) 
/ (나눗셈 연산자)
// (나눗셈 연산자)
% (나머지 연산자)
<< (왼쪽 시프트 연산자)
>> (오른쪽 시프트 연산자)
& (비트 AND 연산자)
| (비트 OR 연산자)
^ (비트 XOR 연산자)
~ (비트 반전 연산자)
< (작음)
> (큼)
<= (작거나 같음)
>= (크거나 같음)
= (같음)
!= (같지 않음)
not (불리언 NOT 연산자)
and (불리언 AND 연산자)
or (불리언 OR 연산자)

'''
#연산자 * ** / + - // %
a = 10
b = 3
#사칙연산
print(a+b)   #13
print(a-b)   #7
print(a/b)   #3.33333..
print(a*b)   #30
print(a**b)  #10^3 = 10*10*10 = 1000
print(a//b)  #3
print(a%b)   #1

#a % 2 == 0 =>2의 배수

#비교연산자
#관계 연산자 
# ==(같다) !=(같지 않다)  >  <   >=   <=  => True or False
a = 100; b =200
print(a==b, a!=b, a > b, a<b, a>=b, a<=b) # F T F T F T
print(a > b)   #T
print(a >= b)  #T
print(a < b)   #F
print(a <= b)  #F
print(a == b)  #F
print(a != b)  #T

#논리연산자 (and or not )  T and F ==> F
# A and B  ,  A or B , not A
# and
print(False and False) #F
print(True and False)  #F
print(False and True)  #F
print(True and True)   #T

# or
print(False or False) #F
print("F or F = ",(a==b)or(a==101)) #F or F = F
print(True or False)  #T
print(False or True)  #T
print(True or True)   #T

# not
print(not(True))      #F
print("not(a==100) = ", not(a == 100))  
print("not(a==100) = %s" %(not(a==100))) #T -> F
print("not(a==100) = {}".format(not(a==100))) #T -> F

c = True
d = False
print( c and d)   # F
print( c or d)    # T
print( not d)     # T
print((a > b) and (a!=b )) # T and T => T
print(bool(1) and bool(0)) # F
print((a>=b) and (not bool(None))) #T


#할당 연산
e = 10
e += 10 #e = e + 10  => 20
e -= 10 #e = e - 10  => 10
e *= 10 #e = e * 10  => 100
e /= 10 #e = e / 10  => 10.0

print(e)

f = 10
f += 2 # 12
f -= 2 # 10
f *= 2 # 20
f /= 2 # 10.0
f %= 2 # 0
f //= 2 # 0
f **= 2 # 0

print(f)

# -------------------------------------
#시프트 연산  <<  >>  
a = 1
print(a<<2) # 4  001(2) -> 100(2)
print(a>>1) # 0  001(2) -> 000(2)
print(a>>3) # 0  001(2) -> 000(2)

g = 2    # 0b0010 2
print(g)
g = g<<2 # 0b1000 8
print(g)
g = g>>1 # 0b0100 4
print(g)

#비트논리연산 &(and)  |(or) ^(xor) ~(not)
a = 5; b = 3 # 0101 & 0011 = 0001
print(a & b) # 1
print(a | b) # 7
print(0b0101 & 0b0011)
print(~5)
print(~0b0101)
print(5^3)   # 6

h = 5 # 0b 0101
i = 3 # 0b 0011

print(h&i) #?  0001
# 0b 0101
# 0b 0011
#    0001
print(h|i) #?  0111
# 0b 0101
# 0b 0011
#    0111 
print(h^i) #?  0110
print(~(-1)) #?

#bit 연산
a = 40
b = 14
print( a & b)
# & / ~
print(bin(a)[2:].zfill(6))
print(bin(b)[2:].zfill(6))
# 101000
# 001110
# ------ And 연산
# 001000

#######################################
# 문제) 15500 => 화폐 10000 5000 1000 500 100 50 10
# 답 : 10000 1장, 5000 1장, 500 1개
money = 15500
m10000 = money // 10000  # 1장
money %= 10000  #money = money % 10000
m5000 = money // 5000
money %= 5000
m1000 = money // 1000
money %= 1000
m500 = money // 500
money %= 500
m100 = money // 100
money %= 100
m50 = money // 50
money %= 50
m10 = money // 10
money %= 10

print("만원권   : {} 장 \n".format(m10000) +
      "오천원권 : {} 장\n".format(m5000) +
      "천원권   : {} 장\n".format(m1000) +
      "500원   : {} 개\n".format(m500) +
      "100원   : {} 개\n".format(m100) +
      "50원    : {} 개\n".format(m50) +
      "10원    : {} 개".format(m10))

