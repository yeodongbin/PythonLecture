# Stack 클래스 정의 - python list 활용
class Stack():
    class Node():
        def __init__(self):
            self.__data = None

        def input(self,data):
            self.__data = data

        def output(self):
            return self.__data

    def __init__(self):
        self.stack = []

    def push(self, data):
        if (self.count()<4):
            self.node = self.Node()
            self.node.input(data)
            self.stack.append(self.node)
        else :
            print("stack is full~~~~ : {}".format(self.count()))
    
    def pop(self):
        node = self.stack.pop(len(self.stack)-1)
        return node.output()

    def count(self):
        count = len(self.stack)
        return count

    def print(self):
        print("[",end='')
        for node in self.stack:
            print(node.output(), end=",")
        print("]")
        
    

if __name__ == '__main__':
    s = Stack()
    s.push('banana')
    s.push('apple')
    print(s.count())
    s.print()

    print(s.pop())
    s.count()
    s.print()
    
    
#  def __init__(self):
#         self.stack = []

#     def is_empty(self):   # 데이터가 없는지 확인
#         if len(self.stack) == 0:
#             return True
#         else:
#             return False

#     def push(self, data):
#         self.stack.append(data)

#     def pop(self):
#         if self.is_empty():
#             return -1
#         return self.stack.pop()

#     def peek(self):        # 최상단 데이터 확인
#         return self[-1]

# if __name__=="__main__":
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)

#     while s:
#         data = s.pop()
#         print(data, end=' ') # 3 2 1
