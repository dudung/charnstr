# import module
from charnstr import analyze

# print help of function
print(help(analyze))
print()

# defin a string
str = "Abcdef abcd aB a"
print(str)

# analyze the string
result = analyze(str)
print(result)

# check type of output
print(type(result))
