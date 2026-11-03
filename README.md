# Self-Balancing Binary Search Tree: Implementation and Comparison

## Project Overview

This project implements and compares a normal Binary Search Tree (BST) and an AVL Tree using patient IDs as keys and patient names as values. It evaluates their performance using different input datasets and sizes.

## Technologies Used

- Python
- VS Code
- Pandas
- Matplotlib

## Project Files

| File | Description |
|---|---|
| `bst.py` | Binary Search Tree implementation |
| `avl_tree.py` | AVL Tree implementation |
| `workload.py` | Generates test datasets |
| `experiments.py` | Runs BST and AVL performance experiments |
| `red_black_tree.py` | Red-Black Tree practical implementation |
| `test_bst.py` | BST testing |
| `test_avl.py` | AVL testing |
| `test_workloads.py` | Workload testing |
| `results.csv` | Experimental results |
| `plot_results.py` | Generates comparison graph |

## Experimental Workloads

Three datasets are used:

1. Sequential data
2. Random permutation
3. Nearly sorted data with approximately 5% random swaps

The experiment uses 1,000, 5,000 and 10,000 nodes.

## Performance Measurements

The following measurements are collected:

- Tree height
- Insertion time
- Average search comparisons
- Number of AVL rotations
- Deletion time
- Height after deleting 20% of nodes

## How to Run

Run the following commands in the terminal:

```bash
python test_bst.py
python test_avl.py
python test_workloads.py
python experiments.py
python plot_results.py
python red_black_tree.py
```

## Conclusion

The experiments demonstrate that AVL Trees maintain a balanced structure and provide more consistent search performance than ordinary BSTs, particularly for sequential and nearly sorted input data.
