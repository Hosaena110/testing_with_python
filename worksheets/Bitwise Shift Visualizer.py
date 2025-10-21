"""
Input an integer and number of shift positions.
num = int(input("Enter an integer: "))
shifts = int(input("Enter number of shift positions: "))
shifted_num = num << shifts
print(shifted_num)


Show results of left shift and right shift.
num = int(input("Enter an integer: "))
shifts = int(input("Enter number of shift positions: "))

left_shift = num << shifts
right_shift = num >> shifts

print("Left shift:", left_shift)
print("Right shift:", right_shift)

Print the binary form before and after.
"""
num = int(input("Enter an integer: "))
shifts = int(input("Enter number of shift positions: "))

print("Original:", bin(num))
print("Left shift:", bin(num << shifts))
print("Right shift:", bin(num >> shifts))
