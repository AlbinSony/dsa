# Python code to read input and process queries
n = int(input())
arr = list(map(int, input().split()))

# Precompute frequencies
hash_map = [0] * 13
for num in arr:
    hash_map[num] += 1

# Process queries
q = int(input())
for _ in range(q):
    number = int(input())
    # Fetch frequency
    print(hash_map[number])
