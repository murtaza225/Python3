def calculate_lcm(num1, num2):
    # Find the maximum of the two numbers
    max_num = max(num1, num2)

    # Initialize the LCM as the maximum number
    lcm = max_num

    while True:
        if lcm % num1 == 0 and lcm % num2 == 0:
            # If the LCM is divisible by both numbers, break the loop
            break
        lcm += max_num

    return lcm

# Example usage
number1 = 12
number2 = 18
lcm = calculate_lcm(number1, number2)
print("LCM of", number1, "and", number2, "is", lcm)
