"""
Auto check if it is a Strong Number in a range. A strong number is a number whose
sum of factorial of digits equals the number itself. Example: 145 → 1! + 4! + 5! =
145
"""

total = 200
fac_list = []

strong_number = []
for number in range(total+1):
    number = str(number)
    for num in number:
        factorial = 1
        num = int(num)
        for num2 in range(1,num+1):
            factorial *= num2
            # print(factorial)
        fac_list.append(factorial)
        # print(fac_list)
    # factorial = 1
    if sum(fac_list) == int(number):
        strong_number.append(int(number))
    fac_list.clear()
print(strong_number)