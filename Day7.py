Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #======== Introduction to Dictionaries =======
>>> # Dictionary is key value pair combination, How to define dictionary: ====> {}
>>> # it is a mutable data type , If you assign any values, you can altered or modified.
>>> alien={'color':'green', 'points':5}
>>> print(alien)
{'color': 'green', 'points': 5}
>>> type(alien)
<class 'dict'>
>>> # data type Examples : # Dict, # str
>>> # key value pair...  Color is key and green is value, for str
>>> #   Req is  how to get individual values on the console...?
>>> print(alien['color']}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> print{alien['color']}
SyntaxError: invalid syntax
>>> print(alien['color'])
green
>>> print(alien['points'])
5
>>> # enhanacement of the code!!
>>> new_point= alien['points']
>>> print(f"you just earned{new_points} points!")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(f"you just earned{new_points} points!")
NameError: name 'new_points' is not defined
>>> print(f "you just earned{new_points} points!" )
SyntaxError: invalid syntax
>>> print(f 'you just earned{new_points} points!')
SyntaxError: invalid syntax
>>> print(f "you just earned{new_points} points!" )
SyntaxError: invalid syntax
>>> print(f "you just earned{new_point} points!" )
SyntaxError: invalid syntax
>>> print(f"you just earned{new_point} points!")
you just earned5 points!
>>> # Starting with an empty dict:
>>> alien_0 = {}
>>> alien_0['color'] = 'yellow'
>>> alien_0['points']= 10
>>> print(alien_0)
{'color': 'yellow', 'points': 10}
>>> # Initialization alien_0 = {}
>>> How to add new key value pairs to the above
SyntaxError: invalid syntax
>>> # How to add new key value pairs to the above
>>> alien_0['x_position']=0
>>> alien_0['y_position']=25
>>> print(alien_0)
{'color': 'yellow', 'points': 10, 'x_position': 0, 'y_position': 25}
>>> # we can add new things to existing dictionary. this will helps to keep on building..
>>> # Rq: how to modify the values,
>>> alien_0['color'] = 'white'
>>> alien_0['points']= 15
>>> print(alien_0)
{'color': 'white', 'points': 15, 'x_position': 0, 'y_position': 25}
>>> # Remove elements from the dict:
>>> del alien_0['y_position']
>>> print(alien_0)
{'color': 'white', 'points': 15, 'x_position': 0}
>>> 