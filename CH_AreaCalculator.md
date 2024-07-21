# Area Calculator 📐

Create a ``calculator.py`` program that calculates the area of one of the following shapes:

1. Square
2. Rectangle
3. Triangle
4. Circle

The program should present a menu for the user to choose which shape to calculate, then ask them for the appropriate values (side, length, width, etc.).

Then, it should calculate the area and print it out.

Here are the area equations for each shape:

    Shape	            Equation
    Square	            area = side^2
    Rectangle	        area = length ∗ width
    Triangle	        area = (height ∗ base)/2
    Circle	            area = π ∗ radius^2 
  
**Note**: For **pi π** in the area of a circle, feel free to either use ``3.14`` or import the ``math`` module to use the ``math.pi`` variable.

***The output should look something like this:***

            ==================
            Area Calculator 📐
            ==================
                1) Triangle
                2) Rectangle
                3) Square
                4) Circle
                5) Quit

            Which shape: 1

            Base: 5
            Height: 6
            The area is 15