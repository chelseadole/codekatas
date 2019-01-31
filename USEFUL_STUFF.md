Useful Python Stuff
===============

Python Built-Ins:
------- 

**Lists**

```python
# Sorting a list: .sort() mutates original list, returns None
my_list.sort() 

# Sorting a list: sorted() creates a new list, returns new list
sorted(my_list)
```
```python
# Looking at list val and idx
for idx, val in ennumerate(my_list):
    print('Index', idx)
    print('Value', val)
```

```python
# Convert list to string
my_list = ['a', 'b', 'c']
''.join(my_list) # "abc"
```

**Dictionaries**

**String Manipulation**

```python
# Convert string to list of CHARACTERS
string1 = "abc"
string2 = "hello world"
list(string1) # ["a", "b", "c"]
list(string2) # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
```


```python
# Convert string to list of WORDS: returns ["a", "b", "c"]
string1 = "abc" 
string2 = "hello world"
string1.split() # ["abc"]
string2.split() # ["hello", "world"]
```

```python
# Formatting values into string
name, cost = "Alex", 500

# .format()
print("{}'s plane tickets will cost ${}.".format(name, cost)) # "Alex's plane tickets will cost $500."

person = {"name": "Chelsea", "age": 23}
print("My name is {name} and I'm {age} years old.".format(**person)) # "My name is Chelsea and I'm 23 years old."

# f-strings
print(f"{name}'s plane tickets will cost ${cost}") # "Alex's plane tickets will cost $500."
print(f"{person['name'].lower()} is my name lowercase.") # "chelsea is my name lowerccase."
print(f"{2 * 2} is 4.") # "4 is 4"

```

```python
# Removing a character from a string. Strings are immutable, so you have to create a new one.
a = "chelsea"
new_a = a.replace("e") # "chlsa"
```

```python
# Remove whitespace from a string
a = "  alex is the best  "

# Remove ALL whitespace
a.replace(" ", "") # "alexisthebest"

# Remove only trailing or leading whitespace
a.strip() # "alex is the best"
```
**Integers**

**Floats**




