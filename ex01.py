celsius = float(input("Temperature value in celsius"))
Fahrenheit  = (celsius*1.8)+32
print(Fahrenheit)

while True:
    celsius_input = input("enter temperature in Celsius or type 'exit' to exit ")
    
    if celsius_input.lower() == 'exit':
        break

    celsius = float(celsius_input)
    Fahrenheit = (celsius*9/5)+32
    print(Fahrenheit)
 
