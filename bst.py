
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.comparisons = 0

    def insert(self, key, value):
        new_node = BSTNode(key, value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif key > current.key:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            else:
                current.value = value
                return

    def search(self, key):
        current = self.root

        while current is not None:
            self.comparisons += 1

            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, key):
        parent = None
        current = self.root

        while current is not None and current.key != key:
            parent = current

            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return

        if current.left is not None and current.right is not None:
            successor_parent = current
            successor = current.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            current.key = successor.key
            current.value = successor.value

            parent = successor_parent
            current = successor

        if current.left is not None:
            child = current.left
        else:
            child = current.right

        if parent is None:
            self.root = child
        elif parent.left == current:
            parent.left = child
        else:
            parent.right = child

    def inorder(self):
        result = []
        stack = []
        current = self.root

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append((current.key, current.value))
            current = current.right

        return result

    def tree_height(self):
        if self.root is None:
            return -1

        stack = [(self.root, 0)]
        max_height = 0

        while stack:
            node, depth = stack.pop()
            max_height = max(max_height, depth)

            if node.left is not None:
                stack.append((node.left, depth + 1))

            if node.right is not None:
                stack.append((node.right, depth + 1))

        return max_height
