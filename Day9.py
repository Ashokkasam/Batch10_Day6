Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Introduction to functions
>>> def = greet():
	
SyntaxError: invalid syntax
>>> def greet_user(): # defining a function and name dec
	""" Diplsay a simple greeting""" # doc string ---> Commenting inside a function
	print("Hello!!")

	
>>> greet_user() # calling a fucntion--> function call
Hello!!
>>> 1. parameters passing
SyntaxError: invalid syntax
>>>  # 1. Parameters passing
 
>>> # 2. arguments declaration/passing ===
>>> # Req : Greet a user who is logging in the site
>>> def greet_user1(username): # parameter --setting up of the parameters
	"" Diplsay a message to the users"""
SyntaxError: invalid syntax
>>> def greet_user1(username): # parameter --setting up of the parameters
	"""Diplsay a message to the users"""
	print(f"Hello!!, {username.title()}")

	
>>> greet_user1('ashok')
Hello!!, Ashok
>>> # Another Example
def greet_user1(username): # parameter --setting up of the parameters
	"""Diplsay a message to the users"""
	print(f"Hello!! Welcome back to amazon, {username.title()}")

	
>>> greet_user1('ashok')
Hello!! Welcome back to amazon, Ashok
>>> # passing arguments:
>>> 1. Positional arguments
SyntaxError: invalid syntax
>>> # 1. Postional arguments, #2 keyword arguments
>>> def describe_pet(animal_type,pet_name): # parameter --setting up of the parameters
	"""Diplsay Information about a pet"""
	print(f"\n I have a {animal_type}")
	print(f"my {animal_type}'s name is {pet_name.title()}.")

	
>>> describe_pet('cat','snowbe;;') # passing in an order --positional arguments

 I have a cat
my cat's name is Snowbe;;.
>>> describe_pet('cat','snowbell')

 I have a cat
my cat's name is Snowbell.
>>> describe_pet('snowbell','cat')

 I have a snowbell
my snowbell's name is Cat.
>>> describe_pet(pet_name = 'snowbell', animal_type='cat'): # Keywords have been included --->***
	
SyntaxError: invalid syntax
>>> describe_pet(pet_name = 'snowbell', animal_type='cat')

 I have a cat
my cat's name is Snowbell.
>>> decribe_pet('cat')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    decribe_pet('cat')
NameError: name 'decribe_pet' is not defined
>>> # to overcome with problem  with one argument...
>>> # How to deficne a default value ,
>>> # Always define the default value at the end of the parameters.
>>> def describe_pet(pet_name, animal_type= 'dog'): # parameter --setting up of the parameters
	"""Diplsay Information about a pet"""
	print(f"\n I have a {animal_type}")
	print(f"my {animal_type}'s name is {pet_name.title()}.")

	
>>> describe_pet('Rambo')

 I have a dog
my dog's name is Rambo.
>>> describe_pet('x','cat')

 I have a cat
my cat's name is X.
>>> describe_pet('x','Bull')

 I have a Bull
my Bull's name is X.
>>> describe_pet('y','OX')

 I have a OX
my OX's name is Y.
>>> # Return values:
>>> def get_formatted_name(first_name, Last_name):
	""" Return a full name, Neatly formatted"""
	full_name = f"{first_name}{last_name}"
	return full_name.title()

>>> get_formatted_name('Ashok Kumar', 'ABCD')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    get_formatted_name('Ashok Kumar', 'ABCD')
  File "<pyshell#47>", line 3, in get_formatted_name
    full_name = f"{first_name}{last_name}"
NameError: name 'last_name' is not defined
>>> def get_formatted_name(first_name, Last_name):
	"""Return a full name, Neatly formatted"""
	full_name = f"{first_name}{last_name}"
	return full_name.title()

>>> get_formatted_name('ashok kumar', 'ka')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    get_formatted_name('ashok kumar', 'ka')
  File "<pyshell#50>", line 3, in get_formatted_name
    full_name = f"{first_name}{last_name}"
NameError: name 'last_name' is not defined
>>> def get_formatted_name(first_name, last_name):
	"""Return a full name, Neatly formatted"""
	full_name = f"{first_name}{last_name}"
	return full_name.title()

>>> get_formatted_name('ashok kumar', 'ka')
'Ashok Kumarka'
>>> get_formatted_name('ashok kumar', 'ABCD')
'Ashok Kumarabcd'
>>> 