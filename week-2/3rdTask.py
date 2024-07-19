def convert_temperature(temp, scale):
    if scale == "C":
        # Convert Celsius to Fahrenheit
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C is {converted_temp}°F.")
        return converted_temp
    elif scale == "F":
        # Convert Fahrenheit to Celsius
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F is {converted_temp}°C.")
        return converted_temp
    else:
        print("Invalid scale. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        return None

# Example usage:
temperature = float(input("Enter the temperature: "))
scale = input("Enter the scale ('C' for Celsius, 'F' for Fahrenheit): ").upper()
converted_temperature = convert_temperature(temperature, scale)
