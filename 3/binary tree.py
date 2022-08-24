# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST


class Node:
	def __init__(self, fai):
		self.left = None
		self.right = None
		self.val = fai

# A utility function to insert
# a new node with the given key


def insert(root, data):
	if root is None:
		return Node(data)
	else:
		if root.val == data:
			return root
		elif root.val < data:
			root.right = insert(root.right, data)
		else:
			root.left = insert(root.left, data)
	return root

# A utility function to do inorder tree traversal


def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)


# Driver program to test the above functions
# Let us create the following BST
#   50
#  /  \
# 30  70
# / \ / \
# 20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inoder traversal of the BST
inorder(r)
