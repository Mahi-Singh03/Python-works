n= int(input("Enter a number: "))

def pattern(n):

    # Base Case
    if n == 0:
        return

    # Recursive Case
    pattern(n - 1)

    print("*" * n)

pattern(n)