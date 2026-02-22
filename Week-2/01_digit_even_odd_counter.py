"""
Given a number, count how many digits are even and how many are odd. Extract
digits using loop logic.
"""
number = 123456789
even, odd = 0,0
number = str(number)
for digit in number:
    digit = int(digit)
    if digit%2==0:
        even+=1
    else:
        odd += 1
print(f"Even = {even}\nOdd = {odd}")