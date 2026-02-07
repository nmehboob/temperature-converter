def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    celsius = kelvin - 273.15
    return celsius

def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    
    choice = input("\nChoose option (1-4): ")
    temp = float(input("Enter temperature: "))
    
    if choice == "1":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")
    elif choice == "3":
        result = celsius_to_kelvin(temp)
        print(f"{temp}°C = {result:.2f}K")
    elif choice == "4":
        result = kelvin_to_celsius(temp)
        print(f"{temp}K = {result:.2f}°C")
    else:
        print("Wrong choice!")

if __name__ == "__main__":
    main()
