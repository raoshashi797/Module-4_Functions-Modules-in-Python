def factorial(n):
    factor = 1
    if n == 1:
        return 1
    else:
       factor = n * factorial(n-1)
    return factor
n = int(input("Enter a number: ")
        )
print(f"Factorial of 5 is {factorial(n)}")