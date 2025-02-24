def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    
    #Check for Non-Numeric values
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("List must contain only numbers.")
        
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 'a']
#try:
#    average = calculate_average(my_numbers)
#    print(f"The average is: {average}")
except TypeError as e:
    print(f"Error: {e}")
