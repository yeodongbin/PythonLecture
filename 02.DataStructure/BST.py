def factorial_01(input):
    n = input + 1
    result = 1
    for i in range(1,n,1):
        result *= i
    return result

# 재귀함수
def factorial_02(input):
    if (input > 1):
        return input * factorial_02(input-1)
    else:
        return 1

print(factorial_01(5))
print(factorial_02(5))


#Root node
#parent node
#child node
#siblings(brother node)
#leaf node(terminal node)

class Node:
  def __init__(self, value):
    self.value = value
    self.left, self.right = None, None
    

    
