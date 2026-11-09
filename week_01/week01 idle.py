Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("hello world")
... print('I am a student and i am learning python')
SyntaxError: multiple statements found while compiling a single statement
>>> [DEBUG ON]
>>> [DEBUG OFF]
>>> 
======================================================== RESTART: C:/Users/pc/Desktop/week01.py ========================================================
hello world
I am a student and i am learning python
>>> 
======================================================== RESTART: C:/Users/pc/Desktop/week01.py ========================================================
hello world
I am a student and i am learning python
>>> 
======================================================== RESTART: C:/Users/pc/Desktop/week01.py ========================================================
hello world
I am a student and i am learning python
4.0
10
0
>>> result_of_addition= 5+5
>>> result_of_addition
10
>>> class(result_of_addition)
SyntaxError: invalid syntax
>>> type(result_of_addition)
<class 'int'>
class Outer:
    def __init__(self):
        self.name = "Outer Class"

def display(self):
    print("This is the inner class")
    outer = Outer()
    print(outer.name)

    
