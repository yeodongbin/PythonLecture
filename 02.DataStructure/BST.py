
#Root node
#Parent node
#Child node
#siblings node
#leaf node
class Node:
    def __init__(self, value = 0):
        self.value = value
        self.left, self.right = None, None

class BST:
    def __init__(self,value=None):
        self.root_node = None
        if (value is not None):
            self.root_node = Node(value)

    def deleteNode(self, node, value):
            if node is None:
                return node

            if value < node.value:
                node.left = self.deleteNode(node.left, value)
            elif(value > node.value):
                node.right = self.deleteNode(node.right, value)
            else:
                if node.left is None:
                    temp = node.right
                    node = None
                    return temp
                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp

                temp = self.get_minValue(node.right)#node.right
                node.value = temp.value
                node.right = self.deleteNode(node.right, temp.value)
            return node

    def insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.value:
            node.left = self.insert(node.left,data)
        else :
            node.right = self.insert(node.right,data)
        return node
    
    def get_minValue(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

    def get_maxValue(self, node):
        current = node
        while(current.right is not None):
            current = current.right
        return current

    def print(self, node):
        if node is not None:
            self.print(node.right)
            print(node.value, ' ', end="")
            self.print(node.left)

if __name__ == "__main__":
    bst = BST()
    bst.root_node = bst.insert(bst.root_node,4) 
    bst.root_node = bst.insert(bst.root_node,2) 
    bst.root_node = bst.insert(bst.root_node,3)
    bst.root_node = bst.insert(bst.root_node,1)
    bst.root_node = bst.insert(bst.root_node,7)
    bst.print(bst.root_node)
    print()

    print(bst.get_minValue(bst.root_node).value)
    print(bst.get_maxValue(bst.root_node).value)

    bst.root_node = bst.deleteNode(bst.root_node, 7)
    bst.print(bst.root_node)
    print()



    
