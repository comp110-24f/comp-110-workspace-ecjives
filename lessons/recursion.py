def factorial(n: int) -> int:
    """Get the factorial of a number 'n'."""
    if n < 0:
        raise ValueError("'n' must be greater than or equal to 0")

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
