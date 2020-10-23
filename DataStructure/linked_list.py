class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            curNode = self.head
            while curNode.next != None:
                curNode = curNode.next
            curNode.next = node

    def print(self):
        curNode = self.head
        string = ""
        while curNode:
            string += str(curNode.data)
            if curNode.next:
                string += " -> "
            curNode = curNode.next
        print(string)

