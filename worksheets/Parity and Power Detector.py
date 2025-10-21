"""

Input an integer.

Print:

Whether it’s even or odd using num & 1

Whether it’s a power of two using (num & (num - 1)) == 0
"""
num = int(input("Enter an integer: "))

if num & 1 == 0:
    print("Even")
else:
    print("Odd")

if num > 0 and (num & (num - 1)) == 0:
    print("Power of two")
else:
    print("Not a power of two")
