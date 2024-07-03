# Forma más convencional de llamar a una variable
my_first_variable = "snake_case"

# 2da forma: corta y en minuscula
nombre = "Roberto"

# 3ra forma convencional de variable
myFirstVariable = "camelCase"

# INCORRECTAS
# first-name = "Rocio"
# first$name = "Rocio"
# first@name = "Rocio"
# num-1 = 12
# 1num = 12

# TIPOS
string_variable = "Juan tiene hambre"
int_variable = 15
bool_variable = True
# Concatenacion de variables en un print
print(string_variable, int_variable, bool_variable)
print("Mi edad es:", int_variable)

#Convertir variable int a str
my_int_to_str_variable = str(int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Muchas variables en una sola linea
name, surname, alias, age = "Rocio", "Schkair", "Rossi", "23"
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)