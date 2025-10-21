# your code here
def miles_to_km(miles):
    return miles * 1.60934

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

choice = input("Type 'm' to convert miles to kilometers or 'c' to convert Celsius to Fahrenheit: ").strip().lower()
value = float(input("Enter the value to convert: "))

if choice == 'm':
    print(f"{value} miles is {miles_to_km(value)} kilometers")
elif choice == 'c':
    print(f"{value}°C is {celsius_to_fahrenheit(value)}°F")
else:
    print("Invalid choice")
