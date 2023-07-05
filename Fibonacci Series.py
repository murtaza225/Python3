def fibonacci(n):
    if n <= 0:
        return "Invalid input. Nth term should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Initialize the first two terms of the series
        term1 = 0
        term2 = 1

        # Calculate the nth term of the series
        for _ in range(3, n + 1):
            term1, term2 = term2, term1 + term2

        return term2

# Example usage
n = 10
nth_term = fibonacci(n)
print("The", n, "term of the Fibonacci series is:", nth_term)
