
def cel_to_fah():
    celsius = float(input("Enter Celsius Value: "))
    fahrenheit = celsius * 9 / 5 + 32
    
    print(f"The converted Celsius temperature is equal to {fahrenheit:.2f}°F. Fahrenheit")
    
def fah_to_cel():
    fahrenheit = float(input("Enter Fahrenheit Value: "))
    celsius = (fahrenheit - 32) * 5 / 9
    
    print(f"The converted Fahrenheit temperature is equal to {celsius:.2f}°C. Celsius")


def cel_to_kelv():
    cellsius = float(input("Enter Celsius Value: "))
    kelvin = cellsius + 273.5
    
    print(f"The converted Celsius temperature is equal to {kelvin:.2f}°K. Kelvin")



while True: 
    print("Temperature converter using python")
    print("")
    
    print("Choose what to convert")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")

    choice = int(input())

    if choice == 1:
        cel_to_fah()
    elif choice == 2:
        fah_to_cel()
    elif choice == 3:
        cel_to_kelv()
    else:
        print("Thank you for using this program! XD")
        break
    