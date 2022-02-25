#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises Solutions
# 
# These are my solutions that I wrote while working on the article [NumPy Examples: Forty-Five Practice Questions To Make You an Expert](https://codesolid.com/numpy-practice-questions-to-make-you-an-expert/).  I've tried to list the original questions in the comments.

# In[1]:


import numpy as np


# ## Array Creation
# 
# NumPy supports a variety of methods for array creation.

# In[2]:


# How would you create a one dimensional NumPy array of the numbers from 10 to 100, counting by 10?

np.arange(10, 110, 10)


# In[3]:


# How could you do the same thing with a standard Python range and a list?

np.array([i for i in range(10, 110, 10)])


# In[4]:


# What does np.array() do (no arguments passed to constructor).  Guess:  exception?

# np.array()


# In[5]:


# How might you construct a NumPy array of capital letters (A-Z) 


# In[6]:


arr = np.array(['fee', 'fi', 'fo', 'fumble-dee-dum'])
arr.dtype


# In[7]:


arr = np.array([chr(i) for i in range(ord('A'), ord('Z') + 1)])
arr.dtype
arr[0].dtype


# In[8]:


# How would you create a ten-element array of all zeros?  
print(np.zeros(10))

# Of all ones?
print(np.ones(10))


# In[9]:


# What is the default data dype for the np.zeros function?
# Guess is float64

df = np.zeros(10)
df.dtype


# In[10]:


# How can you create an array of 10 random integers?

np.random.randint(1, 6, 10)


# In[11]:


# How can you create a normal distribution of 10 numbers, centered on 5? 
# Note, the 1 in center represents mu, size of STD DEV, and is arbitrary.

np.random.normal(5, 1, 10)


# In[12]:


# How can you create an array of 10 random numbers in the range 0 - 1?

np.random.rand(10)


# # Multidimensional arrays
# 

# In[13]:


np.zeros((3, 5))


# In[14]:


myarray = np.arange(1, 13).reshape(3, 4)
myarray


# In[15]:


myarray[1,2]


# In[16]:


myarray.ndim


# In[17]:


myarray.reshape(2,6)


# In[18]:


arr


# In[19]:


myarray.shape


# In[20]:


myarray.reshape(2,6)


# In[21]:


myarray


# In[22]:


x = myarray
x


# In[23]:


x[0,0] = 42
myarray


# In[24]:


# Create a 3x4 array of random integers between 1 and 10 
np.random.randint(1, 11, (3,4))


# In[25]:


# ... or:
    
arr = np.random.randint(1,11,12).reshape(3,4)
arr


# In[26]:


arr - arr


# In[27]:



z_list = [z for z in range(0,5)]
y_list = [z_list for y in range(0,4)]
x_list = [y_list for x in range(0,3)]

x_array = np.array(x_list)


         


# In[28]:


# My guess is x_array.shape == 3,4,5.  Correct but show tuple brackets would be better
x_array.shape


# In[29]:


# What is the value of x_array.ndim?
x_array.ndim


# In[30]:


# Given the following:
arr = np.arange(0,6).reshape(2,3)
arr
# How could you convert it to an array that looks like
# array([[0,3], [1,4], [2,5]))
# My answer either arr.transpose() or arr.T
# (arr.transpose() == arr.T).all()
# Note difference is mutablity?  NO!  Both return a view.  Need to copy.
arr.transpose()


# In[31]:


four_by_five = np.arange(1, 21).reshape(4,5)
four_by_five


# In[32]:


# Write an exoression to return the first row
four_by_five[0]


# In[33]:


# Write an exoression to return the last row
four_by_five[-1]


# In[34]:


# What does four_by_five[2,3] return?  My answer, 14 (scalar)
four_by_five[2,3]


# In[35]:


# What does four_by_five[3,2] return?  My answer, 18 (scalar)
four_by_five[3,2]


# In[36]:


# How could you return the first column?  It will be a (four-element array ending with 16.) My answer four_by_five[:,0]
four_by_five[:,0]


# In[37]:


# What does four_by_five[:, 2:4] return?
# My answer the last two columns -- wrong, third and fourth columns
four_by_five[:, 2:4]


# In[38]:


# Corrected question
# What does four_by_five[:, 3:5] return?
four_by_five[:, 3:5] 


# In[39]:


# Write an expression to return the last two columns of the middle two rows.
four_by_five[1:3, 3:] 


# In[40]:


one_dim = np.arange(1,6)
one_dim


# In[41]:


# What would be the result of one_dim * 2
# My answer array([2, 4, 6, 8, 10])
one_dim * 2


# In[42]:


# What would be the result of one_dim + np.arange(5, 0, -1)?
# My answer:  array([ 6,  6,  6,  6, 6])
one_dim + np.arange(5, 0, -1)


# In[43]:


# How many zeros are in the array returned by one_dim - one_dim ?
# My answer: 5
one_dim - one_dim


# In[44]:


# What is the result of one_dim > 2 ?
# My answer:  array([F, F, T, T, T])  (abbreviated)
one_dim > 2


# In[45]:


# For NumPy arrays, logical operations are done with the operators "&" and "|", 
# rather than the usual Python "and" and "or".  Given that, can you evaluate this expression?  
# (one_dim > 4) | (one_dim == 1)
# My answer: array([True, False, False, False, True])
(one_dim > 4) | (one_dim == 1)


# In[46]:


# What is the result of -one_dim?
# My answer array([-1, -2, -3, -4, -5])
-one_dim


# In[47]:


# np.absolute take the absolute value of each element.  Given that, what would the result be of the following expression:
# My answer 4,5
np.absolute(-(one_dim[3:]))


# In[48]:


# What is returned by one_dim.sum()?
# My answer: 15
one_dim.sum()


# In[49]:


# What is the value of one_dim.mean() ?

print(one_dim)
one_dim.mean() # The median!


# In[50]:


# Given the following...

arr = np.array([0., .5, 1.0, 1.5, 2.0]) * np.pi
arr


# In[51]:


# What are the "approximate" values for 
# np.around(np.sin(arr), 0)
# My answer:  array(0, 1, 0, -1, 0)
np.around(np.sin(arr), 0)


# In[52]:


# What are the approximate values for 
# np.around(np.cos(arr), 0)
# My answer:  array(1, 0, -1, 0, 1)
np.around(np.cos(arr), 0)


# In[53]:


# You're asked to save the following two arrays as is to a file, "data.npz". The arrays should be named as they are here in the file. How could you do it?
people = np.array(["John", "Jenniffer", "Helen", "Miryam"])
languages = np.array([2, 2, 1, 1])
# My answer np.savez("data.npz", people=people, languages=languages)
np.savez("data.npz", people=people, languages=languages)


# In[54]:


# How could you load the files again into two new variables, people2 and languages2

arrays = np.load("data.npz")
people2 = arrays["people"]
languages2 = arrays["languages"]
print(people2)
print(languages2)


# In[55]:


# Given 
# arr = np.arange(1,13).reshape(3,4)
# Save it to a csv file, "myrray.csv".
arr = np.arange(1,13).reshape(3,4)
np.savetxt("myarray.csv", arr, delimiter=",")


# In[56]:


# How would you load it back into arr2?
# My guess: arr2 = np.loadtxt("myarray.csv", delimiter=",")
arr2 = np.loadtxt("myarray.csv", delimiter=",")
arr2


# In[57]:


# Given 

lumberjack = np.array("I'm a lumberjack and I'm OK I sleep all night and I work all day".split(" "))
lumberjack


# In[58]:


# How could you capitalize the first character of each string?
# Guessed np.capitalize(lumberjack) wrong
np.char.capitalize(lumberjack)


# In[59]:


# What would you expect the value of np.char.capitalize(lunberjack)[2] to be?
# My answer "Lumberjack"
np.char.capitalize(lumberjack)[2]


# In[60]:


# How could you surround each string with an initial and final asterisk character (*)?  
# Guessed add takes n arguments, wrong, need two arguments at a time
np.char.add(np.char.add("*", lumberjack), "*")


# In[61]:


# np.where can be used to make selections.  How can we use this to create a smaller array of those strings that have a length >= 5?
# My guess np.where(lumberjack, np.length(lumberjack) >= 5)  Way off.


# In[62]:


np.where(np.char.str_len(lumberjack) >=5)


# In[63]:


lumberjack[np.where(np.char.str_len(lumberjack) >=5)]

