number_string = input("Enter an integer: ")

integer_value = int(number_string)
float_value = float(number_string)
string_value = str(integer_value)

print("Original value:", number_string, "| Type:", type(number_string))
print("Integer value:", integer_value, "| Type:", type(integer_value))
print("Float value:", float_value, "| Type:", type(float_value))
print("String value:", string_value, "| Type:", type(string_value))
