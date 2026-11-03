from avl_tree import AVL

tree = AVL()

for k, v in [(10, "A"), (20, "B"), (30, "C"), (40, "D"), (50, "E"), (25, "F")]:
    tree.insert(k, v)

print("Inorder:", tree.inorder())
print("Height:", tree.tree_height())
print("Is BST:", tree.is_bst())
print("Is balanced:", tree.is_balanced())
print("Rotations:", tree.rotations)
print("Search 30:", tree.search(30))

tree.delete(40)

print("After deletion:", tree.inorder())
print("Balanced after deletion:", tree.is_balanced())
print("BST property after deletion:", tree.is_bst())