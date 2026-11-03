from workloads import generate_workloads

sequential, random_data, nearly_sorted = generate_workloads(20)

print("Sequential:", sequential)
print("Random:", random_data)
print("Nearly sorted:", nearly_sorted)