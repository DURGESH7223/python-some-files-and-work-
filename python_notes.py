# -*- coding: utf-8 -*-

#https://bit.ly/2LMb6sW

#Aditya Hajela
#aspl: 23423
#present/absent

"""
Created on Mon Jul  8 17:50:52 2019

@author: pythor
"""
'''
PYTHON:
    > Its an high level, interpreted, interactive,
      object oriented, scripting language.
    > created by GUIDO van ROSSUM in 1989 but first
      launched in 1991.
    
    > Characteristics:
        open source
        plateform independent
        data types and tools
        library utilities
        3rd party utilities
        dynamic typing
        automatic memory management.
        case sensitive
        everything in python is an object
'''


'''
IDENTIFIERS:
    It is a name to define a variable, function,
    module, class, or any other object.
> you can define an identifier by using,
A-Z, a-z, _ (underscore), followed by digits (0-9),

example for:
    right way to define an identifier:

    A=10
    b=20
    abc=34
    _a='hello'
    _1='world'
    _ab1=78
    a1='universe'

> you cannot define an identifier by using any
metacharacters as like $, %, *, @ etc or only numbers (0-9)
or reserved keywords.

example for:
wrong way to define an identifier:
    
    #=12
    $='hello'
    23=77
    2a=90
    if=89
'''
'''
Reserved Keywords:
    
    if, else, elif, for, while, and, or, not, try,
    except, raise, lambda, finally, yield, as, with

'''

'''
OPERATORS:

Arithmetic (+, -, /, *, %, //, **)
% (modulas) : remainder
// (floor division) : quotient
** (exponent) : power
'''
#a=7
#b=2
#c=a**b
#print(c)

'''
Assignment (=, +=, -=, /=, *=, //=, **=, %=)
'''

#a=3
#b=7
#print(a)
#a**=b
#print(a)
#print(b)

'''
Comparission  (==, <, >, >=, <=, !=)
'''
'''
booleans data type
0 : False
1 : True
'''
#print(2>7)
#print(3==3)
#print(1!=9)
#print(3>=1)

'''
logical (and, or, not)
'''
#if 7>5 or 5!=5:
#    print('hello')
#else:
#    print('bye!')

'''
>> comment in python : #

>> triple  quotes is used for paragraph.

>> python indentation is defined via 
colon (:) symbol.
indentation is alligned by
4 spaces or 1 tab key
> Everything in python is an object.
'''

'''
membership  (in, not in)
'''
#a='hello'
#print('h' in a)
#print('a' not in a)

'''
identity (is, is not)
'''

#print(7 is 7)
#print(7 == 7)
#
#print(10 is not 'hello')
#print(10 != 'hello')
#
#print('hello' is 'bye!')

'''
Variables:
Variables are nothing but reserved 
memory locations to store values. 

It means that when you create a 
variable, you reserve some space 
in the memory.

Based on the data type of a variable, 
the interpreter allocates memory 
and decides what can be stored 
in the reserved memory. 

Therefore, by assigning different 
data types to the variables, 
you can store integers, decimals 
or characters in these variables.
'''

'''
DATA TYPES:
    > Numbers
    > Strings
    > List
    > Tuple
    > Dictionary
    > Set
    > Frozenset
'''

'''
NUMBERS:
> It stores numeric values.
> Not iterable
> Immutable (Unchangeable)
> Types of Numbers data type:
    Integers , Float, Complex
'''
#a=89
#print(a)
#print(type(a))
#
#b=45.7
#print(b)
#print(type(b))
#
#c=3.6+7j
#print(c)
#print(type(c))

'''
STRINGS
> It's defined within single (') or 
double (") quotes.

>Immutable (Unchangeable)
>Iterable
>Sequential
>Ordered
>supports concatenation and repetetion
'''

#a='hello'
#b="world"
#c=a+b
#print(len(a))
#print(c,type(c),type(a),type(b))
#print(a*3)
#print(a)

'''
INDEXING (Addressing) AND SLICING
> this concept is valid for
string, list, tuple data types.
'''

#a='universe'
#print(a)
#print(len(a))
#print(a[1:6])
##print(a[1 :  : 1])
#print(a[::])
#print(a[::2])
##print(a[::-1])
#print(a[:6:2])

'''
data type conversion:
   int()
   float()
   complex()
   str()
   list()
   tuple()
   dict()
   set()
   frozenset()
'''
#a=int(input('enter a first number: '))
#b=int(input('enter second number: '))
#c=a+b
#print(c)

#x=int(input('enter a number: '))
#print(x,type(x))
'''
String's BUILT IN METHODS
'''

a='universe'
#print(a.capitalize())
#print(a.lower())
#print(a.upper())
#print(a.count('e'))
#print(a.isalnum())
#print(a.islower())
#print(a.isupper())
#print(a.replace('e','$'))

#a='my name is aditya'
#print(a.split())
#print(a.split('i'))
#print(len(a))

#a='-'
#b='aditya'
#print(a.join(b))


#a='****hello****'
#print(a.lstrip())
#print(a.strip('*'))
#print(a.rstrip('*'))


'''string formatting
%d : decimal
%s : string
%f : float
'''
#a=15
#b=20
#c=a+b
#print('the sum of a and b is c')
#print('the sum of %d and %d is %d'%(a,b,c))
#print('the sum of {} and {} is {}'.format(a,b,c))


#print('the sum of',a,'and',b,'is',c)


#a=input('enter name: ')
#b=input('enter language: ')
#c=input('enter nationality: ')

#my name is aditya, I am an indian and I am python coder.


#print('my name is %s, I am an %s and I am %s coder.'%(a,c,b))
#print('my name is {0}, I am an {2} and I am {1} coder.'.format(a,b,c))


#x=input('First Name: ')
#y=input('Programming Language: ')
#z=int(input('Active since ? '))
#
#print('\nMy name is {}.\nI program with {} \
#programming language.\nI am doing it \
#since last {} years.'.format(x,y,z))
#
#print('\n')
#
#print('\nMy name is %s.\nI program with %s \
#programming language.\nI am doing it \
#since last %d years.'%(x,y,z))

'''
LIST 
> List consist of mixed & duplicate data types.

> Defined using square [] brackets 
within which all items are comma (,) 
separated.

> Iterable
> Sequential
> Mutable (changeable)
> Ordered 
'''

#a=['c','c++','python','java','julia','cobol','algol-68']
#print(a)
#print(len(a))
#a.sort()
#print(a)
#print(type(a))
#print(len(a))
#
#a[3]=67
#print(a)
#
#del a[3]
#print(a)
#
#print(a[0])
#print(a[-4])
#print(a[1:5])

#b=['hello',43,'bye',45.3,['apple','banana',67],'lotas']
#c=a+b # concatenation
#print(c)
#print(a*2) # repeatetion
#print(b)
#print(b[4][1][0])
#print(b[0][1])

'''
LIST: BUILT IN METHODS
'''
#a.append([1,2,3,4,5])
#print(a)
#
#a.pop(3)
#print(a)
#
#a.pop()
#print(a)

#a.clear()
#print(a)

#c=a.copy()
#print(c)

#a.insert(3,'apple')
#print(a)

#a[3]=70
#print(a)

#a=[45,23,1,4,5,2,2,1,67,45,67,89,33,22]
#print(a)

#a.sort()
#print(a)

#a.sort(reverse=True)
#print(a)

#a.reverse()
#print(a)

#a.remove(2)
#print(a)

'''
TUPLE
> Tuple consist of mixed & duplicate
 data types.
 
> Defined using parenthesis () brackets 
within which all items are 
comma (,) separated.

> Iterable
> Sequential
> Immutable (Unchangeable)
> Ordered 
'''

#a=('c','c++','python','java','julia','cobol','algol-68')
#print(a)
#print(type(a))
#print(len(a))
#print(a[0])
#print(a[4])
#print(a[1:5])
#b=('hello',43,'bye',45.3,['apple','banana',67],'lotas')
#c=a+b # concatenation
#print(c)
#print(a*2) # repeatetion
#print(b)
#print(b[4][1])
#print(b[0][3])

#a[3]=67
#print(a)

#del a[3]
#print(a)

'''
Dictionary {, , ,}
> Iterable
> unordered (it doesn't support indexing 
  and slicing)
> mutable (Changeable)
> it consist of key:value items
> keys must be immutable as values can 
be of any data type.
> per key only one value is allowed
> only one key can be considered within a dict
if given the same key with different value then
the last assignment wins.
'''

#a={'Class':'ML','Age':20,'Name':['Karan','arjun']}
#print(a)
#print(a['Name'])
#print(a.items())
#print(a.keys())
#print(a.values())

#a.clear()
#print(a)

#a.pop('Class')
#print(a)
#
#a.popitem()
#print(a)
#
#a['Class']=[123456,7890]
#print(a)
#
#a[45]='hello'
#print(a)
#
#a[45]='bye'
#print(a)
#
#a.update({'name':'aditya'})
#print(a)
#
#a.update({45:'byeeee!'})
#print(a)


'''
SET
> Iterable
> Mutable
> Unordered
> it does not support duplicate items.
> it does not support indexing and slicing
> it does not consist of mutable items 
(like list)
> it consist of unique individual items.
> consist mixed datatype
'''

#a={1,4,3,2,(3,2,4,5),6,7,6,'hello',7,5,4,6,'hello',7,9,8,8,8,8,9}
#print(a)
#print(type(a))
#print(len(a))
##print(a[6])
#a.add('python') #takes only 1 object
#print(a)
#a.update([2,34],(32,(56,67,'kilo')),{57,54})
#print(a)
#
#a.remove(32)
#print(a)
#a.discard((2,4,5))
#print(a)

#a={45,1,2,67,7}
#b={45,3,2,45,43,2}
#print(a|b) #union
#print(a&b) #intersection
#print(a.__xor__(b)) #difference

'''
Frozenset

> It can be defined using frozenset() method.
> Iterable
> Immutable (unchangeable)
> Unordered
> it does not support duplicate items.
> it does not support indexing and slicing
> it does not consist of mutable items (like list)
> it consist of unique individual items.
> consist mixed datatype
> doesn't support concatenation & repeatetion
'''

#x=[1,2,3,2,1,2,3,2,1,2,3,4,5,6,7,6,5,7]
#a=frozenset(x)
#print(len(x))
#print(x)
#print(type(x))
#print(a)
#print(type(a))
#print(len(a))
#
#b=frozenset({2,3,43,45,45,46,45,32,2,3,7})
#print(b)
#
#c=a.copy()
#print(c)
#
#print(a.difference(b)) #elements of a not in b
#
#print(b.difference(a)) #elements of b not in a
#
#print(a.union(b))
#print(a.intersection(b))
#
#a=frozenset({3,4,5})
#b=frozenset({7,8})
#
#print(a.issubset(b))
#print(b.issubset(a))
#print(a.issuperset(b))
#print(a.isdisjoint(b))
#print(b.isdisjoint(a))

'''
Conditionals

if
elif
else

'''
#a=float(input('enter a no: '))
#print(a)
#print(type(a))

#a=int(input('-->> '))
#if a%2==0:
#    print(a,'is even')
#else:
#    print(a,"is odd")


#a=int(input('-->> '))
#if a>0:
#    print(a,'is positive')
#elif a==0:
#    print(a,'is zero')
#else:
#    print(a,'is negative')
 

#if 7!=7:
#    print('hello')
#elif 34!=34:
#    print('python')
#else:
#    print('bye')


#a=int(input('-->> '))
#if a>0:
#    print(a,'is positive')
#elif a==0:
#    print(a,'is zero')
#else:
#    print(a,'is negative')



'''
WAP to check a user input nos. is:
only divisible by 2
only divisible by 3
divisible by both 2 & 3
not divisible by 2 & 3
'''

#a=int(input('-->> '))
#if a%2==0 and a%3==0:
#    print('divisible by both')
#elif a%2==0:
#    print('only divisible by 2')
#elif a%3==0:
#    print('only divisible by 3')
#else:
#    print('not divisible by both')




#a=int(input('-->> '))
#if a%2==0:
#    if a%3==0:
#        print('both')
#    else:
#        print('only by 2')
#else:
#    if a%3==0:
#        print('only by 3')
#    else:
#        print('not by both')


'''
WHILE LOOP:
> Repeats a statement or group of statements 
  while a given condition is TRUE. 
> It tests the condition before executing the
  loop body.

FOR LOOP:
> Executes a sequence of statements multiple 
  times and abbreviates the code that manages 
  the loop variable.
'''

#a=1
#b=15
#while a<b:
#    if a%2==0:
#        print(a)
#    a+=1
#print('I am out of loop!')



#a=1
#while a<=30:
#    if a%2==0:
#        print(a)
#    a+=1
#print('i\'m out of the loop')

'''
> wap to reverse a string value from user input
> wap to swap two user input nos.
> wap to swap first and last value of a list
> wap to print factorial of user input.
> wap to print nos which are divisible by 7 
  but not a multiple of 5 in a range of 
  2000 to 3200
'''

#a=str(input('-->> '))
#print(a)
#print(a[::-1])

'''
multiple line statement 
'''

#a=b=c=d=10
#print(a,b,c,d)
#
#a,b,c,d=1,2,7,5
#print(a,b,c,d)


#a,b=5,7
#print('a:',a)
#print('b:',b)
##a,b=b,a
#
##c=a
##a=b
##b=c
#
#a=a+b
##a=12
#b=a-b
##b=5
#a=a-b
##a=7
#
#print('a:',a)
#print('b:',b)



#a=[12,'hello',67.78,'bye',67,'apple']
#print(a)
#a[0],a[-1]=a[-1],a[0]
#print(a)

#print(type(a))
#print(len(a))
#print(a[3])

#while 1==1:
#    print('infinity')


#a=[]
#x=0
#n=int(input('how many nos. to input in a list-->> '))
#while x<n:
#    y=int(input('%d: element--> '%x))
#    a.append(y)
#    x+=1
#print(a)


#a=[12,'hello',23,34,(23,45,67,89),'good','bad',34]

#listt=[]
#while 1:
#    n=int(input('1:int, 2:str','3:tuple','4:list','5:exit'))
#    if n==1


#a=5
#x=1
#while a!=0:
#    x=a*x
#    a=a-1
#print(x)


#x=[]
#a=2000
#while a<=3200:
#    if a%7==0 and a%5!=0:
#        x.append(a)
#    a+=1
#print(x)





#for i in range(1,30):
#    if i%2!=0:
#        print(i)


#for i in range(1,30):
#    if i%2==0:
#        print(i,end=' ')


#a=[]
#for i in range(2000,3200):
#    if i%7==0 and i%5!=0:
#        a.append(i)
##        print(i,end=' ')
#print(a)

#while True:
#    print('hello')


#x=0
#a=[34,7,56,34,23,90,99,7]
#print(len(a))
#for i in range(len(a)):
#    x+=a[i]
#print(x/len(a))


#>> wap to check whether a given no is
# prime or not.
# 
#>> wap to get the sum of 
#even 
#negative 
#odd
#from a list

#a=[-9,7,8,9,-7,44,3,-12]



#>> find the largest no. within a list
#>> smallest no in a list
#>> take two list and merge both of them,
#then sort it up.


#a=int(input("enter a no for table: "))
#for i in range(1,11):
#    print(a,'*',i,'=',a*i)



#count=0
#a=int(input('-->> '))
#for i in range(2,a):
#    if a%i==0:
#        count+=1
#if count==0:
#    print(a,'is a prime number')
#else:
#    print(a,'is not a prime number')


#a=[23,56,43,45,77,9,-2,-34,-12,-45,7]
#even=odd=neg=0
#for i in range(len(a)):
#    if a[i]<0:
#        neg+=a[i]
#    elif a[i]%2==0:
#        even+=a[i]
#    else:
#        odd+=a[i]
#print('Sum of Even nos.: ',even)
#print('Sum of Odd nos.: ',odd)
#print('Sum of Neg nos.: ',neg)

#a=[23,56,43,45,77,9,-2,-34,-12,-45,7]
#print(max(a))
#print(min(a))

#a.sort()
#print(a)
#print('max',a[-1])
#print('min',a[0])

#x=a[0]
#for i in range(len(a)):
#    if a[i]>x:
#        x=a[i]
#print(x)


#a=[56,89,560,44,57]
#b=[77,3,8,6,5,3,2,1,78,56]
#c=a+b
#print(c)
#
#c.sort(reverse=True)
#print(c)

'''selection sort algo'''

#sot=[]
#while len(c)!=0:
#    y=c[0]
#    for i in range(len(c)):
#        if c[i]<y:
#            y=c[i]
#    sot.append(y)
#    c.remove(y)
#print(sot)

#a=[]
#for i in range(1,10):
#    x=(i,i*i)
#    a.append(x)
#print(a)


#a=[56,89,560,56,44,57,1,2,3]
#b=[77,3,8,6,5,3,2,1,78,56]
'''union'''
#union=[]
#for i in range(len(a)):
#    if a[i] not in union:
#        union.append(a[i])
#print(union)
#for i in range(len(b)):
#    if b[i] not in union:
#        union.append(b[i])
#print(union)


'''intersection of two list'''
#a=[56,89,560,56,44,57,1,2,3]
#b=[77,3,6,5,3,2,1,78,56]
#inter=[]
#for i in range(len(a)):
#    for j in range(len(b)):
#        if a[i]==b[j]:
#            if a[i] not in inter:
#                inter.append(a[i])
#print(inter)

#a=set(a)
#b=set(b)
#c=a.intersection(b)
#c=list(c)
#print(c)

#a=[[12,7],[3,3],[11,2],[2,0.5],[23,1]]
#sot=[]
#while len(a)!=0:
#    y=a[0][1]
#    for i in range(len(a)):
#        if a[i][1]<y:
#            y=a[i][1]
#    if a[i] not in sot:
#        sot.append(a[i])
#    a.remove(a[i])
#print(sot)
#x=[[2,1,3],[23,1],[11,2],[3,3],[12,7]]


'''FUNCTIONS'''
'''
> A function is a block of organized, 
reusable code that is used to perform a 
single, related action. 

> Functions provide better modularity for 
your application and reusing a high degree 
of code.

>Function block begin with the keyword def
followed by function name and parenthesis().

example-

def addition():
    
> block of code within every function begins
with the colon (:) symbol.

> any input arguments should be placed within
these parenthesis.

> the first statement is an optional doc-string
in which coder can defin the summary of the func.

> then followed by the logic body consisting 
the logical code.

> return statement is followed by the indentation
of the function which is defined at the end of 
the function definition which exits the function.

> return statement is followed by an optional 
expression. if the expression is not defined 
then by default the function returns NONE value.

syntax to define function definition in python-

def func_name(a,b,..n):
    'doc-string'
    ..
    logic body consisting logical operations
    .....
    ...
    return expression
'''

#def str_print(a):
#    'print a value'
#    print(a)
#    return
#str_print('hello world')
#str_print('India successfully launches chandrayaan-2')
#str_print([34,3,2,1,45,67])
#str_print(200)


'''
calling a function-
> function is called by the function name 
followed by parenthesis w.r.t.t argument's 
parameter(value).

> we can also define the parameters (value) within the
definition for the arguments.
'''

'''Addition of two numbers'''

#def add(a,b):
#    'addition of two nos.'
#    c=a+b
#    print('the sum of %d and %d is %d'%(a,b,c))
#    return
#n=int(input('enter the times to use addition function: '))
#for i in range(n):
#    a=int(input('-->>'))
#    b=int(input('-->>'))
#    add(a,b)


#def specific(a):
#    'calculating the sum of even, odd,\
#    negative nos. in a list'
#    even=odd=neg=0
#    for i in range(len(a)):
#        if a[i]<0:
#            neg+=a[i]
#        elif a[i]%2==0:
#            even+=a[i]
#        else:
#            odd+=a[i]
#    print('Sum of Even nos.: ',even)
#    print('Sum of Odd nos.: ',odd)
#    print('Sum of Neg nos.: ',neg)
#    return
#specific([23,56,43,45,77,9,-2,-34,-12,-45,7])
#specific([34,-5,-34,55,33,22,11,-90])

#a=[]
#n=int(input('enter input integer for list values: '))
#for i in range(n):
#    x=int(input('enter values for list: '))
#    a.append(x)
#print('List: ',a)
#def prime(y):
#    'prime nos.'
#    pri=[]
#    nopri=[]
#    for j in range(len(y)):
#        count=0
#        for i in range(2,y[j]):
#            if y[j]%i==0:
#                count+=1
#        if count==0:
#            pri.append(y[j])
#        else:
#            nopri.append(y[j])
#    print('prime: ',pri)
#    print('Not prime: ',nopri)
#    return
#prime(a)

'''FUNCTION ARGUMENTS
> Required
> Keyword
> Default
> Variable Length
'''

#def add(a,b):
#    c=a+b
#    print(c)
#    return
#add(12,23)

'''keywords arguments'''

#def apple(name,age):
#    print('Name: ',name)
#    print('Age: ',age)
#    return
#apple('aditya',10)
#apple(23,'arjun')
#apple(age=30,name='karan')

'''default arguments'''

#def xyz(name,chapter='python'):
#    print('My name is {} and I code in {}'.format(name,chapter))
#    return
#xyz('Aditya')
#xyz('arjun','julia')
#xyz(chapter='c++',name='karan')

'''Variable length arguments'''
#print('\n')
#
#def abc(a,*b):
#    print('output is: ')
#    print('A: ',a)
#    for i in b:
#        print(i)
#    print(type(b))
#    print('\n')
#    return
#abc(10)
#abc('c','c++','python','julia','cobol')


'''lambda function'''


'''scope of variables'''

#a=10
#def rain():
#    a+=20
#    return
#print(a)
#rain()
#print(a)


#a=10
#def rain():
#    a=90
#    a+=20
#    print(a)
#    return
#print(a)
#rain()
#print(a)

#print('\n')


#a=10
#def rain():
#    global a
#    a+=20
#    return
#print(a)
#rain()
#print(a)

'''MODULES'''
'''
> A module allows you to logically organize 
  your Python code. 

> Grouping related code into a module makes 
  code easier to understand and use. 
 
> A module is a Python object with arbitrarily 
  named attributes that you can bind and reference.

> Simply, a module is a file consisting of Python code. 

> A module can define functions, classes and variables.
> A module can also include runnable code.
'''
'''call a module'''

#> import module_name
#> from module_name import fun_1, fun_2,.....fun_N
#> from module_name import *

#import my_library as lib
#
#print(lib.add(45,23))
#print(lib.avg(23,45,67,2,3,4,5,6,7,8,9))


#from my_library import add,fibbo,avg,power
#print(fibbo(0,1,10))
#print(add(45,23))
#print(power(2,3))


#from my_library import *
#print(fibbo(0,1,10))
#print(add(45,23))
#print(power(2,3))
#print(quotient(34,2))

'''ROCK PAPER SCISSOR CONSOLE GAME'''

#import random
#n=int(input('-->> '))
#u=c=d=0
#for i in range(n):
#    comp=random.randint(1,3)
#    user=int(input('rock:1,paper:2,scissor:3\n-->> '))
#    if user==comp:
#        print('DRAW')
#        d+=1
#    elif user==1 and comp==2:
#        print('comp wins')
#        c+=1
#    elif user==2 and comp==1:
#        print('user wins')
#        u+=1
#    elif user==1 and comp==3:
#        print('user wins')
#        u+=1
#    elif user==3 and comp==1:
#        print('comp wins')
#        c+=1
#    elif user==2 and comp==3:
#        print('comp wins')
#        c+=1
#    elif user==3 and comp==2:
#        print('user wins')
#        u+=1
#    print('USER WINS: ',u)
#    print('COMP WINS: ',c)
#    print('DRAW: ',d)

#import random
#a=[12,34,56,22,1,322,89,4,3,2]
#print(a)
#random.shuffle(a)
#print(a)

'''
TIC TAC TOE
CALCULATOR
CODE BREAKER
'''
#while 1:
#    print('Press \n1: add\n2: sub\n3: mul\n4: div')
#    n=int(input('enter your choice: '))
#    if n>0 or n<5:
#        break
#    a=int(input('enter first no.: '))
#    b=int(input('enter second no.: '))
#    if n==1:
#        c=a+b
#        print('the addition of {} and {} is {}'.format(a,b,c))
#    elif n==2:
#        c=a-b
#        print('the subtraction of {} and {} is {}'.format(a,b,c))
#    elif n==3:
#        c=a*b
#        print('the multiplication of {} and {} is {}'.format(a,b,c))
#    elif n==4:
#        print('the division of {} and {} is {}'.format(a,b,c))

'''code breaker'''
#import random
#code=random.randint(0,9)
#while True:    
#    print('secret code is: ',code)
#    print('welcome to game code breaker: \n')
#    guess=int(input('guess the code:\n-->>'))
#    if guess==111:
#        break
#    if guess==code:
#        print('CODE BREAKED')
#        break
#    else:
#        print('WRONG GUESS!!!, TRY AGAIN\nPress: 111 to exit')
    
'''
FILE HANDLING
'''
'''
syntax

obj = open('file_name','access_mode',bufering)

access mode

> 'w' : write
> 'r' : read
> 'a' : append
> 'w+' : write + read
> 'r+' : read + write
> 'a+' : append + read
> 'wb' : write in binary
> 'rb' : read in binary
> 'ab' : append in binary
> 'wb+': (write + read) in binary
> 'rb+': (read + write) in binary
> 'ab+': (append + read) in binary

'''

'''to write the data in the file
obj.write(input)
'''

#a=open('xyz.txt','w',1)
#x=str(input('enter a string value to insert in the file: \n-->> '))
#a.write(x)
#print('file created successfully')
#a.close()

'''
to read the data
obj.read(address)
'''

#a=open('xyz.txt','r',1)
#x=a.read()
#print(x)
#a.close()

#import os
#print(dir(os))
#os.rename('xyz.txt','abc.txt')
#os.mkdir('folder')
#os.rmdir('folder')
#os.rename('folder','new_folder')





