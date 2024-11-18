def convert_temperature(value, unit):
    if unit == 'C':
        return (value * 9/5)+ 32
    elif unit == 'F':
        return (value - 32) * 5/9
    else:
        return "invalid unit"
    
value = float(input("enter the number:"))
unit = input("enter temperature unit ('C' for celcius, 'F' for fahrenheit):")

result = convert_temperature(value, unit)
print(result)

