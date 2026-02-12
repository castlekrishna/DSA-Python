"""
Question:

Take a number from user.
Print whether it is even or odd.
"""
num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is even.")
# else:
#     print(f"{num} is odd")

print(f"{num} is even")if num % 2 == 0 else print(f"{num} is odd")