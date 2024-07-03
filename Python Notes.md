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