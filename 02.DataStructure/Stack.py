# Stack 클래스 정의 - python list 활용
class Stack(list):
    def __init__(self):
        self.stack = []

    def is_empty(self):   # 데이터가 없는지 확인
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()

    def peek(self):        # 최상단 데이터 확인
        return self[-1]

if __name__=="__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    while s:
        data = s.pop()
        print(data, end=' ') # 3 2 1