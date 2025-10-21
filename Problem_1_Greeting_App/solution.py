# your code here
name = input("What is your name? ")
favorite_food = input("What is your favorite food? ")
current_year = int(input("What is the current year? "))
age = int(input("How old are you? "))

birth_year = current_year - age

print(f"Hello, {name}! It's great that you like {favorite_food}.")
print(f"You were born in {birth_year}.")
