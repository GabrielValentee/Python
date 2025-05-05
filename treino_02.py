def celsius_fahrenheit ():
    get_tem_celsius = float(input("Insira a temperatura em celsius: "))
    convert_fah = (get_tem_celsius * 1.8) + 32
    return convert_fah

temp_fah = celsius_fahrenheit ()

print(f"A tempera em fahrenheit é {temp_fah}: ")

def fahrenheit_celsius ():
    get_temp_fahrenheit = float(input("Insira a temperatura em fahrenheit: "))
    convert_celsius = (get_temp_fahrenheit - 32) * 5/9
    return convert_celsius

temp_cel = fahrenheit_celsius()

print(f"A temperatura em celsius é: {temp_cel}")

