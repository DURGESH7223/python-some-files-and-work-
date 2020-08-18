# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 15:03:43 2019

@author: pythor
"""

'''
What are generators in Python?
There is a lot of overhead in building an iterator in Python;
we have to implement a class with __iter__() and __next__() method, 
keep track of internal states, 
raise StopIteration when there was no values to be returned etc.

This is both lengthy and counter intuitive.
Generator comes into rescue in such situations.

Python generators are a simple way of creating iterators. 
All the overhead we mentioned above are 
automatically handled by generators in Python.

Simply speaking, a generator is a function 
that returns an object (iterator) 
which we can iterate over (one value at a time).
'''


'''
How to create a generator in Python?
It is fairly simple to create a generator in Python. 
It is as easy as defining a normal function with yield statement 
instead of a return statement.

If a function contains at least one yield statement 
(it may contain other yield or return statements), 
it becomes a generator function. 
Both yield and return will return some value from a function.

The difference is that, 
while a return statement terminates a function entirely, 
yield statement pauses the function saving all its states 
and later continues from there on successive calls.
'''



'''
Differences between Generator function and a Normal function
Here is how a generator function differs from a normal function.

Generator function contains one or more yield statement.
When called, it returns an object (iterator) 
but does not start execution immediately.

Methods like __iter__() and __next__() are implemented automatically. 
So we can iterate through the items using next().

Once the function yields, 
the function is paused and the control is transferred to the caller.

Local variables and their states are remembered between successive calls.

Finally, when the function terminates, 
StopIteration is raised automatically on further calls.

Here is an example to illustrate all of the points stated above. 
We have a generator function named my_gen() 
with several yield statements.
'''


## A simple generator function
#def my_gen():
#    n = 1
#    print('This is printed first')
#    # Generator function contains yield statements
#    yield n
#
#    n += 1
#    print('This is printed second')
#    yield n
#
#    n += 1
#    print('This is printed at last')
#    yield n
#
## It returns an object but does not start execution immediately.
#a = my_gen()
##next(a)
#### We can iterate through the items using next().
#print(next(a))
###### Once the function yields, the function is paused and the 
######control is transferred to the caller.
#####
###### Local variables and theirs states are remembered between 
######successive calls.
#####
#print(next(a))
#print(next(a))
######
####### Finally, when the function terminates, StopIteration is 
#######raised automatically on further calls.
######
#print(next(a))
#

'''
One interesting thing to note in the above example is that, 
the value of variable n is remembered between each call.

Unlike normal functions, the local variables are not destroyed 
when the function yields. 

Furthermore, the generator object can be iterated only once.

To restart the process we need to create another generator object 
using something like a = my_gen().

Note: One final thing to note is that we can use 
generators with for loops directly.

This is because, 
a for loop takes an iterator and iterates 
over it using next() function. 

It automatically ends when StopIteration is raised. 
Check here to know how a for loop is actually 
implemented in Python.
'''


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

## Using for loop
for item in my_gen():
    print(item)

