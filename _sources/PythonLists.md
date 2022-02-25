---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Python Lists

Python lists are one of its most flexible and widely used data types.  The basic idea of a list is straightforward because most people already know how to use a list in real life.  We might have a list of things to do, for example:

* Finish work project
* Stop at the pharmacy
* Return parrot to the pet store

Here's how easy it is to create a Python list with those items:

```python
todo_list = ["Finish work project", "Stop at the pharmacy", "Return parrot to the pet store"]
print(todo_list)
```

Square brackets tell Python we're dealing with a list.  It's also possible to use a list constructor, ```list()```, but it's more common to use square brackets, as we've done here.  We can even create an empty list that way:

```python
empty = []
print(type(empty))
```

In the case of our to-do list example, we wanted to populate the list in advance, so we included three strings.  Inside the list, we separate each list item with a comma.


## Lists can contain items of any Python type

We can add any Python object to a list -- numbers, strings, dates, user-defined classes, dictionaries -- even other lists.  

We can even mix and match types in a single list, but just as in real life, this isn't something you usually want to do unless the items are related somehow.  It would make the meaning of the list unclear, and it would be hard to write valid code to process the list.

```python
# A list of numbers
prime_numbers = [2,3,5,7]

# The three stooges
stooges = ['Moe', 'Larry', 'Curly']

# A list of lists
all_my_lists = [prime_numbers, stooges]

# An unclear list of mixed types -- bad idea!
some_list = [42, 3.14, "Make some soup", "Yugoslavia"]
```

## Python Lists are Ordered

The elements in a Python list are ordered with numbers beginning with zero.  Most programming languages start counting from zero rather than one, so this is also how C, Java, JavaScript, and many other languages do it. 

The fact that lists are ordered means we can retrieve or change the items of the list if we know where they appear in the list.  

Let's look at several things we can do with lists in the following code segment.  We'll start with a small list of countries to see what we can do.

```python
countries = ['United States', 'Colombia', 'Japan', 'Kenya']

# Get the first country into a variable.  
# Use the list name, the [] operator, and the zero-based index in the list.
usa = countries[0]
print(usa)

# Find the zero based-index of Japan
location = countries.index('Japan')
print("Japan is at index: ", location)

# Find out how many countries are in the list
length = len(countries)
print("There are", length, "countries in the list.")

# Change the last item in the list.
# Since the list counting is zero-based, the index of the last 
# item is the list's length - 1
countries[length - 1] = 'Republic of Kenya'

# Print the list
print(countries)
```
