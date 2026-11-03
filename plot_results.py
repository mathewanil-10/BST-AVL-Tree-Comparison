
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

sequential = df[df["Dataset"] == "Sequential"]

for tree_name in ["BST", "AVL"]:
    subset = sequential[sequential["Tree"] == tree_name]
    plt.plot(subset["N"], subset["Initial Height"], marker="o", label=tree_name)

plt.xlabel("Number of Nodes (N)")
plt.ylabel("Tree Height")
plt.title("BST vs AVL Height - Sequential Dataset")
plt.legend()
plt.grid(True)
plt.savefig("height_comparison.png")
plt.show()
