
from bst import BST
from avl_tree import AVL
from workload import generate_workloads
import random
import time
import math
import csv

sizes = [1000, 5000, 10000]
results = []

for n in sizes:
    sequential, random_data, nearly_sorted = generate_workloads(n)

    datasets = {
        "Sequential": sequential,
        "Random": random_data,
        "Nearly Sorted": nearly_sorted
    }

    for dataset_name, data in datasets.items():

        for tree_name, TreeClass in [("BST", BST), ("AVL", AVL)]:

            tree = TreeClass()

            start = time.perf_counter()

            for key in data:
                tree.insert(key, f"Patient {key}")

            insertion_time = time.perf_counter() - start
            initial_height = tree.tree_height()

            rng = random.Random(42)
            search_keys = rng.sample(data, min(1000, n))

            tree.comparisons = 0

            for key in search_keys:
                tree.search(key)

            average_comparisons = tree.comparisons / len(search_keys)

            rotations_after_insertion = (
                tree.rotations if tree_name == "AVL" else 0
            )

            delete_count = int(n * 0.20)
            delete_keys = random.Random(100 + n).sample(data, delete_count)

            start = time.perf_counter()

            for key in delete_keys:
                tree.delete(key)

            deletion_time = time.perf_counter() - start
            height_after_deletion = tree.tree_height()

            rotations_after_deletion = (
                tree.rotations - rotations_after_insertion
                if tree_name == "AVL" else 0
            )

            if tree_name == "AVL":
                assert tree.is_balanced()
                assert tree.is_bst()

            results.append({
                "Tree": tree_name,
                "Dataset": dataset_name,
                "N": n,
                "Initial Height": initial_height,
                "Floor log2 N": math.floor(math.log2(n)),
                "Insertion Time": round(insertion_time, 6),
                "Rotations During Insertion": rotations_after_insertion,
                "Average Search Comparisons": round(average_comparisons, 2),
                "Deletion Time": round(deletion_time, 6),
                "Rotations During Deletion": rotations_after_deletion,
                "Height After 20% Deletion": height_after_deletion
            })

            print("\nTree:", tree_name)
            print("Dataset:", dataset_name)
            print("Size:", n)
            print("Initial Height:", initial_height)
            print("Floor log2 N:", math.floor(math.log2(n)))
            print("Insertion Time:", round(insertion_time, 6), "seconds")
            print("Rotations During Insertion:", rotations_after_insertion)
            print("Average Search Comparisons:", round(average_comparisons, 2))
            print("Deletion Time:", round(deletion_time, 6), "seconds")
            print("Rotations During Deletion:", rotations_after_deletion)
            print("Height After 20% Deletion:", height_after_deletion)

            if tree_name == "AVL":
                print("AVL Balanced:", tree.is_balanced())
                print("BST Property:", tree.is_bst())

with open("results.csv", "w", newline="") as file:
    fieldnames = results[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("\nAll experiments completed.")
print("Results saved to results.csv")
