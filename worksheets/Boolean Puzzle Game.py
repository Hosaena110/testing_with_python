"""
You’re designing a gate access system. Access is granted only if:

The user is verified (verified == True)

The user has an even ID (id & 1 == 0)

The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
"""
verified = input("Is user verified? (True/False): ").strip() == "True"
user_id = int(input("Enter user ID: "))
flags = int(input("Enter security flag bits (as integer): "))

if verified and (user_id & 1) == 0 and (flags & 0b111) != 0:
    print("Access granted")
else:
    print("Access denied")
