Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Simple stats with Lists
>>> numbers = list(range(1,21))
>>> print(numbers)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> # requirment is  small, Large and sum of total num
>>> min(numbers)
1
>>> max(numbers)
20
>>> sum(numbers)
210
>>> # Clicing of lists:
>>> # slicing of lists .. Slice s nothing but a piece
>>> students = ['sumanth','prashanth','ashok','nam', 'chintu']
>>> print(students[2])
ashok
>>> # I want make 3 people in 1 group, Other 2 People in the second group.. we are slicing of lists. we are making into 2 lists
>>> print(students[])
SyntaxError: invalid syntax
>>> print(students[0,3])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(students[0,3])
TypeError: list indices must be integers or slices, not tuple
>>> print(students[0:3])
['sumanth', 'prashanth', 'ashok']
>>> print(students[0:3]) print(students
			   
SyntaxError: invalid syntax
>>> print(students[0:3]) # always exclusive in the selected criteria
['sumanth', 'prashanth', 'ashok']
>>> print(students[3:5])
['nam', 'chintu']
>>> print(students[3:7])
['nam', 'chintu']
>>> rint(students[3:5]) # (start value, end value, step count)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    rint(students[3:5]) # (start value, end value, step count)
NameError: name 'rint' is not defined
>>> #========
>>>  # Copying a list
 
>>> my_food= ['pizza', 'burger', 'juice']
>>> friends_food = my_food[:]
>>> print(friends_food)
['pizza', 'burger', 'juice']
>>> riends_food = my_food[:] # copying a list here
>>> #============Introduction to tuple datatype:
>>> is immutable type , # can not be changed, can not be altered, If you are values are not going to be changed.
SyntaxError: invalid syntax
>>> # How exactly define a tuple.
>>> # Example for tuple
>>> dimensions = (200,50)
>>> print(dimensions)
(200, 50)
>>> tuple
<class 'tuple'>
>>> dimensions[0]= 250
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dimensions[0]= 250
TypeError: 'tuple' object does not support item assignment
>>> # list mutable, tuple is immutable..... tuple does not support item assignment.
>>> print(dimensions[0])
200
>>> print(dimensions[1])
50
>>> #===========Zen of Python : It is set of rules ========
>>> Import this
SyntaxError: invalid syntax
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> # ====Read the above ===========
>>> ########just guide lines when coding====
>>> # ## pepet rules ##
>>> #pep8 :
>>> python enhancement praposals:
	
SyntaxError: invalid syntax
>>> 1. proper indentation -----