# Function to classify a number as even or odd
def classify_number(num):
    return "Even" if num % 2 == 0 else "Odd"

# Asking for user input
num = int(input("Enter an integer: "))
print(f"The number {num} is {classify_number(num)}.")

# Using a for loop to generate even numbers from 1 to 50
even_numbers = [n for n in range(1, 51) if n % 2 == 0]
print("\nEven numbers from 1 to 50:", even_numbers)

# Using a while loop to print numbers from 10 down to 1
count = 10
print("\nDescending Order:")
while count >= 1:
    print(count, end=' ')
    count -= 1
print()
