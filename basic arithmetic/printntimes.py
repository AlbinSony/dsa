def print_name(i, num):
    if i > num:
        return
    print("ALBIN")
    print_name(i + 1, num)

def main():
    n = int(input("Enter a number: "))
    print_name(1, n)

if __name__ == "__main__":
    main()
