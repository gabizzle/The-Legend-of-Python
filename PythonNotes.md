# Python Notes

## If-Else Statement

### If Statement
- An ``if`` statement is used to test a condition for truth:
    - If the condition evaluates to ``True``, code in the if part is executed.
    - If the condition evaluates to ``False``, code is skipped.

>       if condition:
>           # code inside

For example, ``if`` the grade variable is greater than 60:

>       if grade > 60:
>           print("You passed!")

The code "inside" the if statement must be indented (preferably 2 spaces).

### Else
- An ``else`` clause can be optionally added to an if statement.
    - If the condition evaluates to ``True``, code in the ``if`` part is executed.
    - If the condition evaluates to ``False``, code in the ``else`` part is executed.

>       if grade > 60:
>           print("You passed.")
>       else:
>           print("You failed.")

The code "inside" the ``else`` clause must also be indented.

### Elif
One or more ``elif`` statements (short for "else if") can be optionally added in between the ``if`` and ``else`` to provide additional condition(s) to check. Sometimes two is simply not enough.

>     if grade > 90:
>        print('A')
>     elif grade > 80:
>        print('B')
>     elif grade > 70:
>        print('C')
>     elif grade > 60:
>        print('D')
>     else:
>        print('F')

## Relational Operators
- ``==`` equal to

- ``!=`` not equal to

- ``>`` greater than

- ``<`` less than

- ``>=`` greater than or equal to

- ``<=`` less than or equal to

### Random
We can use the ``.randint()`` function from a module called ``random`` to generate a random number from a range.

## Logical Operators
Logical operators, also known as Boolean operators, combine and evaluate two conditions. They are ``and``, ``or``, and ``not`` operators:
- ``and`` returns``True`` if both conditions are True, and returns ``False`` otherwise.
- ``or`` returns ``True`` if at least one of the conditions is ``True``, and ``False`` otherwise.
- ``not`` returns ``True`` if the condition is ``False``, and vice versa.

## Loop
- In programming, a ``loop`` is used to repeat a block of code until a specified condition is satisfied. It's another incredibly powerful tool that's used a ton!
- People will often use the generic term “iterate” when referring to loops; iterate simply means “to repeat”.
- A ``while`` loop looks very similar to an ``if`` statement. Just like an ``if`` statement, it executes the code if the condition is ``True``.
- However, the difference is that the ``while`` loop will continue to execute the code inside of it, over and over again, as long as the condition is ``True``.
- In other words, instead of executing once if a condition is true, it executes again and again while that condition is true.

## Range
- To loop through a set of code a specified number of times, we can use a ``for`` loop and the ``range()`` function.
- The ``range()`` function returns a sequence of numbers. By default, the sequence starts at 0 and increments by 1, ending at a specified number.

## Lists
Lists are created using square brackets ``[`` and ``]``. And the items are separated by ``,`` commas.
- List items allow duplicate values.
- Lists can have values with different data types.
- There's no limit to how much data a list can hold.

## Index
- List items are changeable, meaning we can update individual items within a list.
- But before we do that, how can we access an individual item within a list? Well, this is where index comes in!
 **index** is an item's position in a list.
- **Python is 0-indexed**, meaning that the indices starts at 0.

        vowels = ['a', 'e', 'i', 'o', 'u']
        # Index:   0    1    2    3    4

- Another thing to note about index is that it can be positive or negative.
- If the index is negative, it starts from -1 (which is the last item of a list) and it goes backwards from there.

        vowels = ['a', 'e', 'i', 'o', 'u']
        # Index:   0    1    2    3    4
        # Index:  -5   -4   -3   -2   -1

## Slicing
- Is there a way to get more than just one individual item? Yep! It's called slicing.- Slicing is where we can access certain parts of a sequence.
- Instead of accessing an item using a single index like ``name[index]``, we can get multiple items by specifying where to start and where to end the range like ``name[start : end]``.

## Built-in Functions (Lists)

Python comes with some built-in functions, including ones specifically for lists.

Here are some examples:
- The ``len()`` function returns the total length of a list.
- The ``max()`` function returns the maximum value in a list.
- The ``min()`` function returns the minimum value in a list.

## List Methods

- ``.append()``	Add an item to the end of the list
- ``.clear()``	Remove all items from the list
- ``.copy()``	Return a shallow copy of the list
- ``.count()``	Return the number of times the value appears in the list
- ``.extend()``	Appends another list to the current list by extending it
- ``.index()``	Returns the index of a value inside the list
- ``.insert()``	Insert an item at a specified position in the list
- ``.pop()``	Remove an item from a specified position in the list
- ``.remove()``	Remove an item from the list based on the value of the item
- ``.reverse()``	Reverses the list in place
- ``.sort()``	Sorts the list in place

## for-in
The first way is using a ``for``-``in`` loop. Here's an example:

        snowfall = [0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8]

        for i in snowfall:
          print(i)

The ``i`` is a variable which represents an item inside the list, each time the loop iterates. This is saying for every item in the ``snowfall`` list, print out the item. The output will be:

        0.3
        0.0
        0.0
        1.2
        3.9
        2.2
        0.8

### Summary
- Lists are used to store different items in a single variable.
- An index is an item's position in a list. Python lists are 0-indexed.
- Slicing can access certain parts of a list with ``name[start:end]``.
- Python has built-in functions like ``len()``, ``max()``, ``min()``.
- Lists have built-in methods like ``.append()``, ``.insert()``, .``remove()``, ``.pop()``.
- We can iterate over a list using ``for``-``in``

## Function

A **function** is a reusable block of code that performs a specific task. To execute this block of code, you just need to know the function's name, followed by a pair of parenthesis ``()``

Built-in functions are 68 functions that come with the Python interpreter available for use. Here are some that you might recognize: ``print()``, ``input()``, ``len()``

User-defined functions are functions we define ourselves to do a specific task, and it's a two-step process: 
        1. define
        2. call

To define a function, we need a function definition. A function definition begins with the ``def`` keyword, followed by the function name, a set of parentheses, and a colon in that order.

        def name():
        # The code inside

- The ``def`` keyword.
- The function name, followed by a pair of parentheses ``()``.
- The colon ``:``.

The code inside the function is called the body of the function. And just like ``if`` statements and ``while`` loops, the code inside a function must be ***indented***

Note: The common naming convention for functions is ``snake_case``

Suppose we want to create a function named ``say_hello()``:

Defining a function creates the function, and it's the first step, but it doesn't mean that Python will automatically run the code inside its body. How do we convey to Python that we want the function body executed? **We need to call the function!**

        def say_hello():
           print('Howdy! 🤠')
           print('How are you?')

        say_hello()

To **call** a function, we use the function name followed by parentheses somewhere in the code

## Parameters & Arguments

**Parameters** are variables that a function takes in as input. They go inside the parentheses in the function definition and are used inside the function.

An **argument** is the value sent to the function when the function is called.

        def happy_birthday(name):
           print('Happy birthday to you')
           print('Happy birthday to you')
           print('Happy birthday dear ' + name )
           print('Happy birthday to you')

        happy_birthday('Pochita')

- ``name`` is the parameter
- ``Pochita`` is the argument

## Return Value

The ``return`` keyword is used to terminate a function and output a value:

        def function_name():
        # The code inside
        return value

- The return keyword is used to terminate a function and output a value
- When a return statement is reached, Python will stop the execution of the current function, sending a value out to where the function was called.

``print()`` functions can be anywhere in the program — inside or outside of a function, whereas ``return`` is the output of a function; you don't need to print out whatever you are returning.

***As a rule of thumb:***

- Use ``return`` in a function when you want to send value(s) from one point in the code to another.
- Use ``print()`` in a function when you want to display some text to the user.

add(a, b) that adds two numbers a and b.
subtract(a, b) that subtracts two numbers a and b
multiply(a, b) that multiplies two numbers a and b.
divide(a, b) that divides two numbers a and b.
exp(a, b) that takes a to the exponent (or power) of b.

## Scope

**Scope** determines where in the program a variable is visible and can be used.

Here are two types of scope:

- The scope of the ``answer`` variable is only inside the ``add()`` function. It is a local variable that belongs to the local scope of the ``add()`` function.
- Now, a variable created outside of a function is called a **global variable** and belongs to the **global scope**, meaning that they can be used by every function.

## Class

With **classes**, we can create our own data type and use them to model everyday objects with their own unique characteristics and behaviors.

Classes serve as a template for the objects created using that class. Simply put, a class is like a blueprint. A class can make a bunch of objects with identical sets of attributes, similar to how a car manufacturer can use a model blueprint to build hundreds of cars in different colors, interiors, wheels, etc.

In our example, 📜 (class) ➡️ 👩🏼‍💻👨🏻‍💻👩🏽‍💻👩‍💻🧑🏾‍💻 (objects).

The ``class`` keyword following a class name creates the class. By convention, the class name is **capitalized**

        class Student:
        name = ''
        year = 0
        gpa = 0.0
        enrolled = False

The Student class has four attributes:

``.name`` of the type ``str`` (text string)

``.year`` of the type ``int`` (integer number)

``.gpa`` of the type ``float`` (decimal number)

``.enrolled` of the type ``bool`` (boolean value)

## Objects

An **object** is an "instance" of a class. A class is simply a template to create objects, which are individual copies of the class with actual values.

## The ``__init__()`` Method

Using ``__init__()`` in our class definition lets us construct objects with unique attributes. When we create a new ``Student()`` object, we can pass in values for each attribute to **initialize** the new object, all in a single line!

So if we reformat our Student class with ``__init__()``:

        class Student: 
        def __init__(self, name, year, gpa, enrolled):
        self.name = name
        self.year = year
        self.gpa = gpa
        self.enrolled = enrolled

        daniel = Student('Daniel Li', 10, 4.0, True)

Note that ``__init__()`` also uses a separate parameter called ``self``. This represents the object we'll create out of Student(). We need to include ``self`` whenever we want to use ``__init__()``. It's always the first parameter.

## Instances

        class Student: 
                def __init__(self, name, year, enrolled, gpa):
        self.name = name
        self.year = year
        self.enrolled = enrolled
        self.gpa = gpa
        
        def display_info(self):
                print('The student ' + self.name + '\'s GPA is ' + str(self.gpa) + '!')

        mitsuha = Student('宮水三葉', 11, False, 4.0)
        taki = Student('立花瀧', 11, True, 3.8)

        mitsuha.display_info()
        taki.display_info()

        # Output:
        # The student 宮水三葉's GPA is 4.0!
        # The student 立花瀧's GPA is 3.8!

Note: Take a look at def display_info(self). Like what we learned about with the __init__() method, the first argument in the methods we make is always self. Every method has to have this self argument. The object attached to the method call is what self refers to.

In our example, we created two objects, mitsuha and taki.

When we called the ``mitsuha.display_info()`` method, the self parameter refers to the mitsuha object.
In the case of ``taki.display_info()``, self refers to the taki object.

## Modules

A **module** is any file with a .py extension. But more ideally, a module contains statements, functions, and class definitions that revolve around a similar purpose.

- By default, Python comes with over 200 modules that we can use.

Here are some examples:

- ``random`` module to generate a random number.
- ``math`` module to calculate the square root.
- ``datetime`` module to work with dates and times.

### Random Choices

        import random

        dice = [1, 2, 3, 4, 5, 6]

        print(random.choices(dice))
- The``import`` keyword is used to access the random module.
- The ``.choices()`` method will randomly select a single item by default.

We can also set how many items are randomly chosen with the k parameter:

        import random

        dice = [1, 2, 3, 4, 5, 6]

        print(random.choices(dice, k=3))

- This will return a new list of three items randomly selected from dice. Every time you run it, the output should be different.
- **Note**: The ``k`` parameter only sets the length of the returned list from ``.choices()``. This means that a list item may be included in the returned list more than once.

### Multiple Modules

There are two ways to import two or more modules at the top of our program:

With multiple import statements:
        
        import random
        import math

        # Rest of the code...

With one import statement and modules separated by commas:
        
        import random, math

        # Rest of the code...

These two code blocks do the exact same thing.

## ``from``

At the top of our file, this keyword goes before the ``import`` keyword:

        from module_name import objects

We can use the from keyword to import one or more objects from a module, such as built-in classes, methods, or variables.

The next example uses the from keyword to import random module's ``.sample()`` method that returns a list of values randomly picked from another list:
from random import sample

        famous_houses = [
        '🐺 Stark',
        '🐉 Targaryen',
        '🦌 Baratheon',
        '🦑 Greyjoy',
        '🦁 Lannister'
        ]

        example = sample(famous_houses, 2)

        print(f'Example: {example}')

Since the ``.sample()`` method was directly imported, we can just write sample() instead of the usual random.sample().

By the way, more than one method, variable, or class can be imported from a module on a single line.

If we want to import both the .choice() and .sample() methods:

        from random import choice, sample

Note: The ``random.choice()`` method randomly selects and returns a single element from a list.

## ``as``

We can nickname a module by using the as keyword. This is called aliasing.

        import random as rd

From this point of the program, the random module will be known as rd.

The from and as keywords can also be combined:

from random import sample as samp

        example = samp(['Stark', 'Targaryen', 'Baratheon', 'Greyjoy', 'Lannister'], 2)

        print('Example: ' + example[0] + ' ' + example[1])

Instead of typing sample(), we can use the alias we assigned it to, samp().

## ``datetime`` module

The ``datetime`` module specializes in dates and times. Just like ``random``, it comes with Python by default and can simply be imported.

The ``datetime`` module has a date object that accepts the following properties:

``.year``: An integer between 1 and 9999.
``.month``: An integer between 1 and 12.
``.day``: An integer between 1 and the number of days in a given month.

The syntax for a ``date`` is ``datetime.date(year, month, day)``, like so:

        import datetime

        release_date = datetime.date(1991, 2, 20)
        print(release_date)     # Output: 1991-02-20

The output shows the date object with a dash between each part. Also, any single number gets a leading zero 0.

The ``.year``, ``.month``, and ``.day`` properties can be accessed like with any other class object:

        print(f'Python was released in {release_date.year}.')
        # Output: Python was released in 1991.

Retrieving the current date is possible with the ``date.today()`` method:

        datetime.date.today()

