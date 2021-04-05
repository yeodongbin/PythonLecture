class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def create_node(data):
    node = Node(data)
    node.left = None
    node.right = None
    return node

def destroy_node(node):
    node = None

def destroy_tree(node = None):
    if (type(node) != Node):
        return
    
    destroy_tree(node.left)
    destroy_tree(node.right)
    destroy_tree(node)

# Preorder Traversal => DFS 유사
def preorder_print_tree(self, node):
    if type(node) != Node:
        return
    
    print("{} ".format(node.data), end=", ")
    preorder_print_tree(self, node.left)
    preorder_print_tree(self, node.right)

# inorder Traversal
def inorder_print_tree(self, node):
    if type(node) != Node:
        return
    
    inorder_print_tree(self, node)
    print("{} ".format(node.data), end=", ")
    inorder_print_tree(self, node)

# Postorder Traversal
def postorder_print_tree(self, node):
    if type(node) != Node:
        return
    
    postorder_print_tree(self, node)
    postorder_print_tree(self, node)
    print("{} ".format(node.data), end=", ")

if __name__ == "__main__":
    pass
