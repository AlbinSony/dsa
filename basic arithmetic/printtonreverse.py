def print_numbers(num, i):
    if num < i:
        return
    print(num)
    print_numbers(num - 1, i)

n = int(input("Enter a number: "))
print_numbers(n, 1)
