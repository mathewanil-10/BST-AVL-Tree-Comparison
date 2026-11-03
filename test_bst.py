from bst import BST

tree = BST()

tree.insert(10, "John")
tree.insert(20, "Mary")
tree.insert(30, "David")
tree.insert(40, "Alex")

print("Inorder:", tree.inorder())
print("Height:", tree.tree_height())
print("Search 20:", tree.search(20))

tree.delete(20)

print("After deletion:", tree.inorder())
print("Height after deletion:", tree.tree_height())