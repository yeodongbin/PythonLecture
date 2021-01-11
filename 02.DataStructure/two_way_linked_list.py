class TwoWayLinkedList:
    class Node:
        def __init__(self):
            self.__data = None
            self.right = None
            self.left = None
        def input(self,data):
            self.__data = data
        def output(self):
            return self.__data

    def __init__(self, head = None):
        self.head = head
        self.tail = None
        self.current = None
        self.node_count = 0

    def insert(self,index,data):
        node = self.Node()
        node.input(data)

        if self.count() <= 0:
            self.head = node
            self.tail = node
        else :
            if index == 0:
                self.head.left = node
                node.right = self.head
                self.head = node
            elif index == (self.count()):#last
                self.tail.right = node
                node.left = self.tail
                self.tail = node
            else :
                self.current = self.head
                for i in range(0,index):
                    self.current = self.current.right

                self.current.right = node
                node.left = self.current
                node.right = self.current.right
                self.current.right.left = node
        self.node_count+=1
    
    def delete(self, index):
        if (self.node_count == 1):
            if (index == 0):
                self.head = None
            else :
                print(f"node의 갯수가 {self.node_count}개입니다.")
                print(f"index값을 0으로 설정해 주세요.")
        elif (self.node_count > 1):
            if (index == 0): #first
                self.head = self.head.right
                self.head.left = None
            elif (index == (self.node_count-1)): #last
                self.tail = self.tail.left
                self.tail.right = None
            else : #middle
                self.current = self.head
                for i in range(0,index):
                    self.current = self.current.right
                self.current.left.right = self.current.right
                self.current.right.left = self.current.left
        else :
            print(f"node의 갯수가 {self.node_count}개입니다.")

    def print(self):
        self.current = self.head
        print('[',end=" ")
        while self.current:
            print(self.current.output(),end=', ')
            if (self.current.right==None):
                break
            self.current = self.current.right
        print(']')

    def count(self):
        return self.node_count

if __name__ == "__main__":
    ll = TwoWayLinkedList()
    ll.insert(0,'a')
    ll.insert(1,'b')
    ll.insert(2,'c')

    ll.print()
    
