#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises Solutions
# 
# These are my solutions that I wrote while working on the article [NumPy Examples: Forty-Five Practice Questions To Make You an Expert](https://codesolid.com/numpy-practice-questions-to-make-you-an-expert/).  I've tried to list the original questions in the comments.

# In[ ]:


import numpy as np


# ## Array Creation
# 
# NumPy supports a variety of methods for array creation.

# In[ ]:


# How would you create a one dimensional NumPy array of the numbers from 10 to 100, counting by 10?

np.arange(10, 110, 10)


# In[ ]:


# How could you do the same thing with a standard Python range and a list?

np.array([i for i in range(10, 110, 10)])


# In[ ]:


# What does np.array() do (no arguments passed to constructor).  Guess:  exception?

# np.array()


# In[ ]:


# How might you construct a NumPy array of capital letters (A-Z) 


# In[ ]:


arr = np.array(['fee', 'fi', 'fo', 'fumble-dee-dum'])
arr.dtype


# In[ ]:


arr = np.array([chr(i) for i in range(ord('A'), ord('Z') + 1)])
arr.dtype
arr[0].dtype


# In[ ]:


# How would you create a ten-element array of all zeros?  
print(np.zeros(10))

# Of all ones?
print(np.ones(10))


# In[ ]:


# What is the default data dype for the np.zeros function?
# Guess is float64

df = np.zeros(10)
df.dtype


# In[ ]:


# How can you create an array of 10 random integers?

np.random.randint(1, 6, 10)


# In[ ]:


# How can you create a normal distribution of 10 numbers, centered on 5? 
# Note, the 1 in center represents mu, size of STD DEV, and is arbitrary.

np.random.normal(5, 1, 10)


# In[ ]:


# How can you create an array of 10 random numbers in the range 0 - 1?

np.random.rand(10)


# # Multidimensional arrays
# 

# In[ ]:


np.zeros((3, 5))


# In[ ]:


myarray = np.arange(1, 13).reshape(3, 4)
myarray


# In[ ]:


myarray[1,2]


# In[ ]:


myarray.ndim


# In[ ]:


myarray.reshape(2,6)


# In[ ]:


arr


# In[ ]:


myarray.shape


# In[ ]:


myarray.reshape(2,6)


# In[ ]:


myarray


# In[ ]:


x = myarray
x


# In[ ]:


x[0,0] = 42
myarray


# In[ ]:


# Create a 3x4 array of random integers between 1 and 10 
np.random.randint(1, 11, (3,4))


# In[ ]:


# ... or:
    
arr = np.random.randint(1,11,12).reshape(3,4)
arr


# In[ ]:


arr - arr


# In[ ]:



z_list = [z for z in range(0,5)]
y_list = [z_list for y in range(0,4)]
x_list = [y_list for x in range(0,3)]

x_array = np.array(x_list)


         


# In[ ]:


# My guess is x_array.shape == 3,4,5.  Correct but show tuple brackets would be better
x_array.shape


# In[ ]:


# What is the value of x_array.ndim?
x_array.ndim


# In[ ]:


# Given the following:
arr = np.arange(0,6).reshape(2,3)
arr
# How could you convert it to an array that looks like
# array([[0,3], [1,4], [2,5]))
# My answer either arr.transpose() or arr.T
# (arr.transpose() == arr.T).all()
# Note difference is mutablity?  NO!  Both return a view.  Need to copy.
arr.transpose()


# In[ ]:


four_by_five = np.arange(1, 21).reshape(4,5)
four_by_five


# In[ ]:


# Write an exoression to return the first row
four_by_five[0]


# In[ ]:


# Write an exoression to return the last row
four_by_five[-1]


# In[ ]:


# What does four_by_five[2,3] return?  My answer, 14 (scalar)
four_by_five[2,3]


# In[ ]:


# What does four_by_five[3,2] return?  My answer, 18 (scalar)
four_by_five[3,2]


# In[ ]:


# How could you return the first column?  It will be a (four-element array ending with 16.) My answer four_by_five[:,0]
four_by_five[:,0]


# In[ ]:


# What does four_by_five[:, 2:4] return?
# My answer the last two columns -- wrong, third and fourth columns
four_by_five[:, 2:4]


# In[ ]:


# Corrected question
# What does four_by_five[:, 3:5] return?
four_by_five[:, 3:5] 


# In[ ]:


# Write an expression to return the last two columns of the middle two rows.
four_by_five[1:3, 3:] 


# In[ ]:


one_dim = np.arange(1,6)
one_dim


# In[ ]:


# What would be the result of one_dim * 2
# My answer array([2, 4, 6, 8, 10])
one_dim * 2


# In[ ]:


# What would be the result of one_dim + np.arange(5, 0, -1)?
# My answer:  array([ 6,  6,  6,  6, 6])
one_dim + np.arange(5, 0, -1)


# In[ ]:


# How many zeros are in the array returned by one_dim - one_dim ?
# My answer: 5
one_dim - one_dim


# In[ ]:


# What is the result of one_dim > 2 ?
# My answer:  array([F, F, T, T, T])  (abbreviated)
one_dim > 2


# In[ ]:


# For NumPy arrays, logical operations are done with the operators "&" and "|", 
# rather than the usual Python "and" and "or".  Given that, can you evaluate this expression?  
# (one_dim > 4) | (one_dim == 1)
# My answer: array([True, False, False, False, True])
(one_dim > 4) | (one_dim == 1)


# In[ ]:


# What is the result of -one_dim?
# My answer array([-1, -2, -3, -4, -5])
-one_dim


# In[ ]:


# np.absolute take the absolute value of each element.  Given that, what would the result be of the following expression:
# My answer 4,5
np.absolute(-(one_dim[3:]))


# In[ ]:


# What is returned by one_dim.sum()?
# My answer: 15
one_dim.sum()


# In[ ]:


# What is the value of one_dim.mean() ?


one_dim.mean() # The median!


# In[ ]:


# Given the following...

arr = np.array([0., .5, 1.0, 1.5, 2.0]) * np.pi
arr


# In[ ]:


# What are the "approximate" values for 
# np.around(np.sin(arr), 0)
# My answer:  array(0, 1, 0, -1, 0)
np.around(np.sin(arr), 0)


# In[ ]:


# What are the approximate values for 
# np.around(np.cos(arr), 0)
# My answer:  array(1, 0, -1, 0, 1)
np.around(np.cos(arr), 0)


# In[ ]:


# You're asked to save the following two arrays as is to a file, "data.npz". The arrays should be named as they are here in the file. How could you do it?
people = np.array(["John", "Jenniffer", "Helen", "Miryam"])
languages = np.array([2, 2, 1, 1])
# My answer np.savez("data.npz", people=people, languages=languages)
np.savez("data.npz", people=people, languages=languages)


# In[ ]:


# How could you load the files again into two new variables, people2 and languages2

arrays = np.load("data.npz")
people2 = arrays["people"]
languages2 = arrays["languages"]
print(people2)
print(languages2)


# In[ ]:


# Given 
# arr = np.arange(1,13).reshape(3,4)
# Save it to a csv file, "myrray.csv".
arr = np.arange(1,13).reshape(3,4)
np.savetxt("myarray.csv", arr, delimiter=",")


# In[ ]:


# How would you load it back into arr2?
# My guess: arr2 = np.loadtxt("myarray.csv", delimiter=",")
arr2 = np.loadtxt("myarray.csv", delimiter=",")
arr2


# In[ ]:


# Given 

lumberjack = np.array("I'm a lumberjack and I'm OK I sleep all night and I work all day".split(" "))
lumberjack


# In[ ]:


# How could you capitalize the first character of each string?
# Guessed np.capitalize(lumberjack) wrong
np.char.capitalize(lumberjack)


# In[ ]:


# What would you expect the value of np.char.capitalize(lunberjack)[2] to be?
# My answer "Lumberjack"
np.char.capitalize(lumberjack)[2]


# In[ ]:


# How could you surround each string with an initial and final asterisk character (*)?  
# Guessed add takes n arguments, wrong, need two arguments at a time
np.char.add(np.char.add("*", lumberjack), "*")


# In[ ]:


# np.where can be used to make selections.  How can we use this to create a smaller array of those strings that have a length >= 5?
# My guess np.where(lumberjack, np.length(lumberjack) >= 5)  Way off.


# In[ ]:


np.where(np.char.str_len(lumberjack) >=5)


# In[ ]:


lumberjack[np.where(np.char.str_len(lumberjack) >=5)]

