"""Assessment 3.3: Non-Linear Data Structure
Binary Tree built from the last name TAPIC (level-order insertion).

        T
       / \
      A   P
     / \
    I   C
"""
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(letters):
    """Insert letters level by level (left to right)."""
    if not letters:
        return None
    root = Node(letters[0])
    queue = deque([root])
    i = 1
    while i < len(letters):
        current = queue.popleft()
        current.left = Node(letters[i])
        queue.append(current.left)
        i += 1
        if i < len(letters):
            current.right = Node(letters[i])
            queue.append(current.right)
            i += 1
    return root


def bfs(root):
    """Breadth-First Search (level-order) using a queue."""
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def dfs_preorder(node, result=None):
    """DFS: Root -> Left -> Right."""
    if result is None:
        result = []
    if node:
        result.append(node.data)
        dfs_preorder(node.left, result)
        dfs_preorder(node.right, result)
    return result


def dfs_inorder(node, result=None):
    """DFS: Left -> Root -> Right."""
    if result is None:
        result = []
    if node:
        dfs_inorder(node.left, result)
        result.append(node.data)
        dfs_inorder(node.right, result)
    return result


def dfs_postorder(node, result=None):
    """DFS: Left -> Right -> Root."""
    if result is None:
        result = []
    if node:
        dfs_postorder(node.left, result)
        dfs_postorder(node.right, result)
        result.append(node.data)
    return result


if __name__ == "__main__":
    root = build_tree(list("TAPIC"))
    print("Binary Tree for TAPIC")
    print("BFS (level-order):", " -> ".join(bfs(root)))
    print("DFS pre-order    :", " -> ".join(dfs_preorder(root)))
    print("DFS in-order     :", " -> ".join(dfs_inorder(root)))
    print("DFS post-order   :", " -> ".join(dfs_postorder(root)))