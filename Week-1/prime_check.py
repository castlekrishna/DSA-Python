"""
Check whether number is prime or not.
"""
num = int(input("Enter number: "))
flag = True
if num < 2:
    flag = False
for i in range (2,num):
    if num % i ==0:
        flag = False
        break

if flag==False:
    print("Not prime")
else:
    print("Prime")