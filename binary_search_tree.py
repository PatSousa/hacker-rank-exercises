""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    return check_in_order(root, None, None)


def check_in_order(node, min, max):
    if not node:
        return True
    if ((min and node.data <= min) or (max and node.data >= max)):
        return False
    if ((not check_in_order(node.left, min, node.data)) or (not check_in_order(node.right, node.data, max)):
        return False
    return True