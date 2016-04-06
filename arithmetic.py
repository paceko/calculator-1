def add(num1, num2):
    """ Returns the sum of the two input integers"""
    total = num1 + num2 
    return total 

def subtract(num1, num2):
    """Returns the second number subtracted from the first"""
    total = num1 - num2
    return total

def multiply(num1, num2):
    """Multiplies the two inputs together"""
    total = num1 * num2
    return total

def divide(num1, num2):
    """Divides the first input by the second, returning a floating point"""
    total = float(num1) / num2
    return total

def square(num1):
    """Returns the square of the input"""
    total = num1 ** 2
    return total

def cube(num1):
    """Returns the cube of the input"""
    total = num1 ** 3
    return total

def power(num1, num2):
    """Raises the first integer to the power of the second integer and returns the value."""
    return num1 ** num2

def mod(num1, num2):
    """Returns the remainder when the first integer is divided by the second integer"""
    modu = num1 / num2
    remainder = num1 - (num2 * modu)
    return remainder
