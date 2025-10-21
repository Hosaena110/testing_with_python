# your code here
age = int(input("Enter your age: "))
has_license = input("Do you have a license? (yes/no): ").strip().lower()

if age >= 18 and has_license == "yes":
    print("Eligible for the role")
else:
    print("Not eligible for the role")
