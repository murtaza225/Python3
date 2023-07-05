def is_armstrong_number(number):
    # Convert the number to string to calculate the number of digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate the sum of digits raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    return sum_of_digits == number

# Example usage
number = 88909

if is_armstrong_number(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
