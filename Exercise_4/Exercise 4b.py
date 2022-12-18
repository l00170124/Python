conversion = 273.15 
my_temp_in_kelvin = [273.15,294.15, 300, 310.15, 373.15, 400, 500, 600, 700, 800] 
my_temp_in_celsius = [(temp - conversion) for temp in my_temp_in_kelvin] 
print(my_temp_in_celsius)

my_temp_in_kelvin = [273.15,294.15, 300, 310.15, 373.15, 400, 500, 600, 700, 800] 
my_temp_in_fahrenheit = [((temp - conversion) * 1.8 + 32) for temp in my_temp_in_kelvin] 
print(my_temp_in_fahrenheit)