# charnstr
analyze a string for its characters information


## example
Following lines of code

```python
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
```

will produce

```
Help on function analyze in module charnstr.charnstr:

analyze(string)
    Analyze unique characters from a string

    :param str string: The string to be analyzed
    :return: Information of unique characters and count of each
    :rtype: dict

None

Abcdef abcd aB a
{'A': 1, 'B': 1, '_': 3, 'a': 3, 'b': 2, 'c': 2, 'd': 2, 'e': 1, 'f': 1}
<class 'dict'>
```

that tells unique characters buit the given string and number of each of them.
