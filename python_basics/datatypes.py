
# Creating variables of different data types
integer_var = 42
float_var = 3.14
complex_var = 2 + 3j
list_var = [1, 2, 3, 4]
tuple_var = (5, 6, 7, 8)
dict_var = {"name": "Oliver", "age": 20}
set_var = {9, 10, 11}
bool_var = True

# Printing the type of each variable
print(f"Type of integer_var: {type(integer_var)}")
print(f"Type of float_var: {type(float_var)}")
print(f"Type of complex_var: {type(complex_var)}")
print(f"Type of list_var: {type(list_var)}")
print(f"Type of tuple_var: {type(tuple_var)}")
print(f"Type of dict_var: {type(dict_var)}")
print(f"Type of set_var: {type(set_var)}")
print(f"Type of bool_var: {type(bool_var)}")

# Converting integer to float and vice versa
int_to_float = float(integer_var)
float_to_int = int(float_var)

# Printing the results of conversion
print(f"\nConverted integer_var to float: {int_to_float}")
print(f"Converted float_var to int: {float_to_int}")
