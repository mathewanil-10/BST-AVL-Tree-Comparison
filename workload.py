import random

def generate_workloads(n, seed=42):
    sequential = list(range(1, n + 1))

    rng = random.Random(seed)

    random_data = sequential.copy()
    rng.shuffle(random_data)

    nearly_sorted = sequential.copy()
    swaps = int(n * 0.05)

    for _ in range(swaps):
        a = rng.randint(0, n - 1)
        b = rng.randint(0, n - 1)
        nearly_sorted[a], nearly_sorted[b] = nearly_sorted[b], nearly_sorted[a]

    return sequential, random_data, nearly_sorted