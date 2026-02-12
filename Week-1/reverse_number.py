"""
Example:
Input: 1234
Output: 4321
"""
remainder =0
result = 0
num = int(input(("Enter a number: ")))
while num  >0:
    remainder = num %10
    result = result * 10 + remainder #took hint
    
    num = num // 10
print(result)