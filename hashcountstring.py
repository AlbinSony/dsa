# Input a string
s = input().strip()

# Initialize frequency array
hash = [0] * 26

# Count frequency of each letter
for char in s:
    hash[ord(char) - ord('a')] += 1

# Answer queries
q = int(input())
for _ in range(q):
    c = input().strip()
    print(hash[ord(c) - ord('a')])
