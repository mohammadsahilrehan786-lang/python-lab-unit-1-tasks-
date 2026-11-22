n = int(input("Enter a positive integer: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    total = n * (n + 1) // 2
    print("Sum of first", n, "natural numbers =", total)
