class node():
    def __init__(self, value):
        self.value = value

        self.left_child = None
        self.right_child = None
        
    def set_right_child(self, right_child):
        self.right_child = right_child
    def set_left_child(self, left_child):
        self.left_child = left_child


def tranvers(root):
    if root.left_child != None:
        tranvers(root.left_child)
    
    print(root.value, end=', ')

    if root.right_child != None:
        tranvers(root.right_child)


def invert(root):
    queue = [root]
    current_node = root

    while (len(queue)):
        current_node = queue.pop(0)

        l = current_node.left_child
        r = current_node.right_child
        
        if (r != None): queue.append(r)
        if (l != None): queue.append(l)

        current_node.left_child = r
        current_node.right_child = l


root = node(1)
root.left_child = node(2)
root.right_child = node(3)

root.left_child.right_child = node(4)
root.right_child.left_child = node(5)

tranvers(root)
print()


invert(root)
tranvers(root)
