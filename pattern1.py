def print_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

num = int(input("Enter number of rows: "))
print_pattern(num)
