class ListQueue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def push(self,data):
        self.queue.append(data)

    def get(self):
        if not self.isEmpty:
            print("Queue is empty")
        else:
            return self.queue.pop(0)



if __name__=="__main__":
    q = ListQueue()
    q.push(1)
    q.push(2)
    q.push(3)

    print(q.get())
    print(q.get())
    print(q.get())
