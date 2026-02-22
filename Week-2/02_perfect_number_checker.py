"""
Given a number, check if it is a Perfect Number. A number is perfect if the sum of its
proper divisors equals the number itself. Example: 6 → 1 + 2 + 3 = 6
"""

number = int(input("Enter a number: "))
divisor = []
for num in range(1,number):
    if number%num == 0:
        divisor.append(num)
if sum(divisor) == number:
    print(f"{number} is a Perfect Number")
else:
    print(f"{number} is NOT a Perfect Number")

