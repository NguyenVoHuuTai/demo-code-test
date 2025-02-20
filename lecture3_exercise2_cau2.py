m = int(input("Enter the number: "))
n = int(input("Enter the number: "))

if m > n:
    for i in range(1, n + 1):
        if m % i == 0 and n % i == 0:
            gcd = i
    print("The greatest common divisor of", m, "and", n, "is", gcd)
if n > m:
    for i in range(1, m + 1):
        if m % i == 0 and n % i == 0:
            gcd = i
    print("The greatest common divisor of", m, "and", n, "is", gcd)