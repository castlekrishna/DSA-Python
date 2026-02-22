"""
Given a number, check if it is a Strong Number. A strong number is a number whose
sum of factorial of digits equals the number itself. Example: 145 → 1! + 4! + 5! =
145
"""
number = input("Enter a number: ")
fac_list = []
factorial = 1

for num in number:
    num = int(num)
    for num2 in range(1,num+1):
        factorial *= num2
    fac_list.append(factorial)
    factorial = 1
if sum(fac_list) == int(number):
    print(f"{number} is a strong number")
else:
    print(f"{number} is NOT a strong number")
