#!/usr/bin/env python
# coding: utf-8

# # Coding Exercises for Python Lists for Beginners
# 
# Here are the runnable exercises for [Python Lists for Beginners](https://codesolid.com/python-lists-for-beginners/).

# #1. Create a list of three of your favorite foods. Save it in a variable called foods.

# In[1]:


# Your code here:


# #2. From your list of favorite foods, select the second item.

# In[ ]:





# #3. Using a slice, create a __reversed__ copy of your list of favorite food

# In[ ]:





# #4. ```my name is john".upper()``` returns the string "MY NAME IS JOHN".  Given that fact, create an uppercase list of your favorite foods using a for loop.

# In[ ]:





# #5. Create a second uppercase list of your favorite foods, using a list comprehension.

# For exercises 6-14, use the following list as your starting point.  (Tip:  If you run the cell below, you can use the variables in cells beneath).

# In[2]:


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


# #6. Use a function to get the length of the letters list.  Display it.

# In[ ]:





# #7. Get the last item in the list, using a positive index.

# In[ ]:





# #8. Get the last item in the list, using a negative index.

# In[ ]:





# #9. Write a slice expression to return the letters D through F (inclusive)

# In[ ]:





# #10. Write a slice expression that returns the following list: ['A', 'E', 'G']

# In[ ]:





# #11. Based on what you learned in exercise 4, can you guess how to write a program to return a list of lowercase letters based on the letters list?

# In[ ]:





# #12. For #11, did you iterate the list using a list comprehension or a for loop? Why?

# #13. How could you return a copy of the list using a slice expression?

# In[ ]:





# #14. How could you return a list that looks like the list below?
# 
# ```python
# ['G', 'F', 'E', 'D', 'C', 'B', 'A']
# ```

# In[ ]:





# #15. The range function returns a sequence — that is to say, it can be used as you would use a list inside a for-loop or list comprehension. For example:
# 
# ```python
# num_list = [x for x in range(1,6)]
# print(num_list)
# ```
# 
# Output:
# ```python
# [1, 2, 3, 4, 5]
# ```
# 
# Based on what you know about slice syntax, what would you expect the output of the following code to be?

# In[ ]:





# #16. What do you predict will be printed by the code below?
# 
# ```python
# num_list = [x for x in range(1,6)]
# num_list[0:2] = [99, 100]
# print(num_list)
# ```

# In[ ]:





# #17. Here’s a slight variation on the code from #16. What do you expect will be printed by the following code?
# 
# ```python
# num_list = [x for x in range(1,6)]
# other_list = num_list[:]
# other_list[0:2] = [99, 100]
# print(num_list)
# ```

# In[ ]:




