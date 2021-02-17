class LinkedList:
    class Node:
        def __init__(self):
            self.__data = None
            self.right = None
        def input(self,data):
            self.__data = data
        def output(self):
            return self.__data

    def __init__(self, head = None):
        self.head = head
        self.current = None
        self.node_count = 0

    def insert(self, data):
        node = self.Node()
        node.input(data)

        if self.count() <= 0:
            self.head = node
        else :
            self.current = self.head
            while self.current:
                if ( self.current.right==None):
                    self.current.right = node
                    break
                self.current = self.current.right
        self.node_count+=1
    
    def delete(self, index):
        if (self.node_count == 1):
            if (index == 0):
                self.head = self.head.right
            else :
                print(f"node의 갯수가 {self.node_count}개입니다.")
                print(f"index값을 0으로 설정해 주세요.")
        elif (self.node_count > 1):
            if (index == 0): #first
                self.head = self.head.right
            elif (index == (self.node_count-1)): #last
                self.current = self.head
                for i in range(0,(self.node_count)):
                    if (i == (self.node_count-2)):
                        self.current.right = None
                        break
                    self.current = self.current.right
            else : #middle
                self.current = self.head
                for i in range(0,(self.node_count)):
                    if (i == index):
                        before.right = self.current.right
                        break
                    before = self.current
                    self.current = self.current.right
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
          
#     def print(self):
#         curNode = self.head
#         string = ""
#         while curNode:
#             string += str(curNode.data)
#             if curNode.next:
#                 string += " -> "
#             curNode = curNode.next
#         print(string)

    def count(self):
        count = 0
        self.current = self.head
        if self.current == None:
            count = 0
        else :
            while self.current:
                count+=1
                if (self.current.right==None):
                    break
                self.current = self.current.right
        return count

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.print()
    
    ll.delete(1) 
    ll.print()
    
    ll.delete(0)
    ll.print()
