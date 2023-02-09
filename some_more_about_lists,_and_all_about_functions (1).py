# -*- coding: utf-8 -*-
"""Some more about lists, and all about functions

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rKmIuOR8uJZbuUwDvCRUgz648mJJObtE

### Review from Tuesday

- Lists
"""

# how to check if something is in a List


# This is what I called the list when I started to make the notebook. But it is BAD! Why?
L = [1, 2, 3]

# Let's try that again ... 
three_numbers = [1, 2, 3]   

2 in three_numbers
3 in three_numbers
8 in three_numbers

"""- Write a function to count the number of unique data types in a list.
- Hint: use "in"
"""

def count_number_of_unique_data_types(a_list: list) -> int:

    counter = 0
    typessofar: list = []

    for element in a_list:
      if type(element) not in typessofar:
        typessofar.append(type(element))
        counter += 1
        
    return counter

count_number_of_unique_data_types([1,3,"okay",True,4.7])

"""### Unpacking a list

- Python has some neat syntax that allows you to "unpack" a list into variables.
"""

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat

print(color)

"""### Sets 

Checking if something is in a list over an over gets annoying. Sets can help. More broadly, picking good data types can make your life way easier as a programmer. Pay attention to types! It's half the battle.

- A set is an unordered collections of objects
- You create a set like this
"""

animals = set()
animals.add("dog")
animals.add("cat")
animals.add("dog")

animals

"""- What do you think is in the set above? Try it!"""

# Your code here

"""- What happens if you pass a list to the function set?"""

set(["dog", "cat", "dog"])   # what will happen ?

# You can go the other way too 

list(animals)

"""Lists and sets can both be described as a **collection**. A collection is like it sounds, a collection of things."""

# the syntax to make a set is a little different 

majors = set()
majors.add("Biology")
majors.add("English")
majors.add("Business")

majors

"""Try writing the same as above but as a list"""

list(majors)

"""### Interview grading 

For interview grading today, try correcting the pair sum count code from Tuesday so that it returns the correct answer. Hint: use sets. 

This is also a good chance to learn about some of practical tools in modern programming. 

1. Instead of turning in text to Canvas work with a partner to copy your code into a `.py` file. A `.py` file is a text file that ends in `.py` and runs python code. It stores Python code that runs. You should do this using a text editor like Sublime Text or VSCode. A text editor edits text files.
2. One person from your pair should make a repo on GitHub, invite their partner to join, and upload the pairs `.py` file to the repo. Turn in a link to your GitHub repo on Canvas.
"""

from typing import List  # this is needed for one of the type hints 


def pair_sum_count(numbers: List[int], A: int):
    '''
    Count the unique pairs in numbers that add up to A

    Inputs:
        - numbers: a list of numbers
        - A: a number
    Output:
        - the count of unique pairs in the numbers list that add up to A
    '''
    numberset = set()
    counter = 0

    for number_one in numbers:
        for number_two in numbers:
            if number_one not in numberset:
              if number_two not in numberset:
                if number_one + number_two == A:
                  numberset.add(number_one)
                  numberset.add(number_two)
                  counter += 1
    return counter

pair_sum_count([1,2,3,4,5,6,7], 5)

"""#### Galaxy brain addition

- [Galaxy Brain](https://knowyourmeme.com/memes/galaxy-brain)
- Do the youth still use Galaxy Brain?

- What is addition? 
- No really, like what is addition?
- What does it mean to add two lists?
- What do you think will happen?
"""

# test your hypothesis here

"""- Can you make a list of lists in Python? Try it!"""

# your code here

"""- Getting the length of a list"""

spam = ["cat", "bat", "dog", "cat"]
len(spam) # get the length of spam

"""### Quick aside: format strings"""

name = "Fausta"
template = f"Hi, {name}" # notice the f
template

## Write a format string that prints a students GPA 

# YOUR CODE HERE

# Why is this better than concatenating a number and a string?

"""Quick aside: division"""

4/2 == 2

3/4

"""Quick aside: integers and floats"""

a = 4 
type(a)

b = 6.2
type(b)

b.is_integer()

(8/3).is_integer()

"""### Functions

- We've seen functions for a few weeks but never really focused on them directly.
- This is because you need to know how to use functions to get started.
- In programming, this is sometimed described as a "head first" approach, because you learn to swim by being tossed head first into the pool. 
- It's a good way to learn fast, but now it is time to take a slower look at functions

### Why functions?
"""

print("Hi Fausta")
print("Welcome to INFO 2430")


print("Hi Jeremy")
print("Welcome to INFO 2430")


print("Hi Yanick")
print("Welcome to INFO 2430")

def greet(name: str) -> str:
    print(f"Hi {name}")
    print("Welcome to INFO 2430")
    # This function is missing something. 
    # Finish the funciton

"""### Fun with terms

- It is easy to get mixed up when talking about functions 
- Keeping your terms straight helps a lot

- **Define**
- **Call**
- **Pass**
- **Parameter**
- **Argument**


- Use these terms for the function above

### What is return doing?

- This is how I grade your homeworks ...
"""

def add_one(number: int) -> int:
  return number + 1

a = add_one(2)
b = add_one(a)
c = add_one(b)

# what is c?

"""### Keyword arguments

- When **calling** a function you can use keyword arguments
- I like keyword arguments
- It prevents getting mixed up
"""

def greet(name: str, course: str): 
    print(f"Hi {name}")
    print(f"Welcome to INFO {course}")

greet(name="Joe", course="3220")

greet(course="3220", name="Joe")

