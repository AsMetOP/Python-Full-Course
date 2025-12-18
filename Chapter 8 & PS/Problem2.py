def fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celcius = float(input("Enter the degree:"))
print(f"{celcius} degrees in fahrenheit : {fahrenheit(celcius)}")
