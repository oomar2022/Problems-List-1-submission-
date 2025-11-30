# Temperature Converter Python program

tem_Celsius = float(input("Enter temperature in Celsius: "))

if tem_Celsius>0:
    tem_Fahrenheit = tem_Celsius * 1.8 + 32
    print("Temperature in Fahrenheit:",tem_Fahrenheit)

else:
    tem_Kelvin = tem_Celsius + 273.15
    print("Temperature in Kelvin:",tem_Kelvin)