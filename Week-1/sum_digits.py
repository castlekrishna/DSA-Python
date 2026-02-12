"""
Example:
Input: 1234
Output: 10
"""
res = 0
num = int(input("Enter a number: "))
# print(num%10)
while num !=0:
    rem = num%10
    res += rem
    
    num%10
    num = num // 10
print(res)