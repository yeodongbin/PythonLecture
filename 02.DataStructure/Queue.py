class Queue():
    class Node():
        def __init__(self):
            self.__data = None

        def input(self,data):
            self.__data = data

        def output(self):
            return self.__data

    def __init__(self):
        self.queue = []

    def push(self, data):
        if (self.count()<4):
            self.node = self.Node()
            self.node.input(data)
            self.queue.append(self.node)
        else :
            print("queue is full~~~~ : {}".format(self.count()))
    
    class popError(Exception):
        def __init__(self, error_str):
            print(error_str)

    def pop(self):
        try:
            if (self.count() <= 0 ):
                raise self.popError('queue에 데이터가 없습니다.')
            else:
                node = self.queue.pop(0)
        except self.popError:
            return None
        return node.output()

    def count(self):
        count = len(self.queue)
        return count

    def print(self):
        print("[",end='')
        for node in self.queue:
            print(node.output(), end=",")
        print("]")

if __name__ == '__main__':
    s = Queue()
    s.push('banana')
    s.push('apple')
    s.push('mango')
    s.push('strawberry')
    s.push('cow')
    print(s.count())
    s.print()

    print(s.pop())
    s.count()
    s.print()
    


# class ListQueue(object):
#     def __init__(self):
#         self.queue = []

#     def isEmpty(self):
#         if len(self.queue) == 0:
#             return True
#         else:
#             return False

#     def push(self,data):
#         self.queue.append(data)

#     def get(self):
#         if not self.isEmpty:
#             print("Queue is empty")
#         else:
#             return self.queue.pop(0)



# if __name__=="__main__":
#     q = ListQueue()
#     q.push(1)
#     q.push(2)
#     q.push(3)

#     print(q.get())
#     print(q.get())
#     print(q.get())
