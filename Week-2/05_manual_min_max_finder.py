"""
Given a list of numbers, find:
• Largest element
• Second largest element
• Smallest element
Without using built-in functions such as max() or min().
"""

def maximum(numbers):
    maximum = numbers[0]
    for element in numbers:
        if maximum <= element:
            maximum = element
    return maximum
def minimum(numbers):
    minimum = numbers[0]
    for element in numbers:
        if minimum>=element:
            minimum = element
    return minimum
def second_largest(numbers):
    numbers = (sorted(numbers))
    return numbers[-2]

numbers = [23,65,3435,4432,5667,434,8786,232,78,124]
print(f"Maximum: {maximum(numbers)}")
print(f"Minimum: {minimum(numbers)}")
print(f"Second Largest: {second_largest(numbers)}")
