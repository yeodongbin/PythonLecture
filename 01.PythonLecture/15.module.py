import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


##################################################

#import pizza                         #1
#from pizza import make_pizza         #2
#from pizza import make_pizza as mp   #3
#import pizza as p                    #4
#from pizza import *                  #5
import os
import random

if __name__ == '__main__':
    #pizza.make_pizza(12, 'cheese', 'ham') #1
    #make_pizza(12, 'cheese', 'ham')       #2
    #mp(12, 'cheese', 'ham')               #3
    #p.make_pizza(12, 'cheese', 'ham')     #4
    #make_pizza(16, 'potato', 'cheese', 'shrimp')
    print(os.getcwd())  # 파일 호출
    print(random.randint(1, 10))
    
    