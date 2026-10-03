num = int(input("enter the number "))
orig = num
sum = 0 
digit = len(str(num))

for n in str(num):
    sum = sum + (int(n)**digit)

if sum == orig:
    print(" the number is armstrong number ")
else:
    print("the number is not armstrong number ")