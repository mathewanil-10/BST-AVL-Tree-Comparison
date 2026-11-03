
class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class AVL:
    def __init__(self):
        self.root = None
        self.rotations = 0
        self.comparisons = 0

    def get_height(self, node):
        if node is None:
            return -1
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def update_height(self, node):
        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

    def right_rotate(self, y):
        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        self.update_height(y)
        self.update_height(x)

        self.rotations += 1
        return x

    def left_rotate(self, x):
        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        self.update_height(x)
        self.update_height(y)

        self.rotations += 1
        return y

    def rebalance(self, node):
        self.update_height(node)
        balance = self.balance_factor(node)

        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def insert_node(self, node, key, value):
        if node is None:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self.insert_node(node.left, key, value)
        elif key > node.key:
            node.right = self.insert_node(node.right, key, value)
        else:
            node.value = value
            return node

        return self.rebalance(node)

    def insert(self, key, value):
        self.root = self.insert_node(self.root, key, value)

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
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete_node(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self.delete_node(node.left, key)

        elif key > node.key:
            node.right = self.delete_node(node.right, key)

        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            successor = self.find_min(node.right)
            node.key = successor.key
            node.value = successor.value
            node.right = self.delete_node(node.right, successor.key)

        return self.rebalance(node)

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def inorder(self, node=None):
        result = []
        stack = []
        current = self.root if node is None else node

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append((current.key, current.value))
            current = current.right

        return result

    def tree_height(self):
        return self.get_height(self.root)

    def is_balanced(self):
        def check(node):
            if node is None:
                return True

            if abs(self.balance_factor(node)) > 1:
                return False

            return check(node.left) and check(node.right)

        return check(self.root)

    def is_bst(self):
        def check(node, minimum, maximum):
            if node is None:
                return True

            if minimum is not None and node.key <= minimum:
                return False

            if maximum is not None and node.key >= maximum:
                return False

            return (
                check(node.left, minimum, node.key)
                and check(node.right, node.key, maximum)
            )

        return check(self.root, None, None)
