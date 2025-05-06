import itertools

# Function to generate permutations
def generate_permutations(data):
    return list(itertools.permutations(data))

# Example usage
items = ['A', 'B', 'C']
perms = generate_permutations(items)

# Print results
print(f"Permutations of {items}:")
for p in perms:
    print(p)
