r"""
Assessment 3.6: DFS Methods in Tree
Binary tree built from the first name (ARJNE) and last name (TAPIC).
Letters are placed level by level (left to right):

              A
          /       \
         R         J
       /   \     /   \
      N     E   T     A
     / \   /
    P   I C
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(letters):
    """Build a binary tree level by level from a list of letters."""
    nodes = [Node(ch) for ch in letters]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0]


def preorder(node, result):
    """Root -> Left -> Right"""
    if node:
        result.append(node.data)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


def inorder(node, result):
    """Left -> Root -> Right"""
    if node:
        inorder(node.left, result)
        result.append(node.data)
        inorder(node.right, result)
    return result


def postorder(node, result):
    """Left -> Right -> Root"""
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.data)
    return result


if __name__ == "__main__":
    first_name = "ARJNE"
    last_name = "TAPIC"

    root = build_tree(list(first_name + last_name))

    print("Tree letters :", first_name + last_name)
    print("PreOrder     :", " ".join(preorder(root, [])))
    print("InOrder      :", " ".join(inorder(root, [])))
    print("PostOrder    :", " ".join(postorder(root, [])))