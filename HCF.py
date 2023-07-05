def calculate_gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

# Example usage
number1 = 24
number2 = 36
gcd = calculate_gcd(number1, number2)
print("GCD of", number1, "and", number2, "is", gcd)
