"""
Auto check perfect number. A number is perfect if the sum of its
proper divisors equals the number itself. Example: 6 → 1 + 2 + 3 = 6
"""

total = int(input("Enter a number: "))
divisor = []
perfect_number = []
print(f"Finding perfect number till {total}")
for number in range(1,total+1):
    for num in range(1,number):
        if number%num == 0:
            divisor.append(num)
            # print("number: ",number,divisor)
    if sum(divisor) == number:
        perfect_number.append(number)
    divisor.clear()
print("Perfect numbers are: ",perfect_number)

