def add(*args):
    """ Returns the sum of the two input integers"""
    total = 0
    for arg in args:
        total = total + arg # total += arg
    return (total)

def subtract(num1, num2):
    """Returns the second number subtracted from the first"""
    return num1 - num2 
    # total = 0
    # for arg in args:
    #     num1 = arg
    #     total = num1
    #     print "test 1"
    #     break

    # for arg in args:
    #         total = total - arg 
    #         print "test 2"
    # return (total) 

def multiply(num1, num2):
    """Multiplies the two inputs together"""
    return num1 * num2

def divide(num1, num2):
    """Divides the first input by the second, returning a floating point"""
    return float(num1) / num2

def square(num1):
    """Returns the square of the input"""
    return num1 ** 2

def cube(num1):
    """Returns the cube of the input"""
    return num1 ** 3

def power(num1, num2):
    """Raises the first integer to the power of the second integer and returns the value."""
    return float(num1) ** float(num2)

def mod(num1, num2):
    """Returns the remainder when the first integer is divided by the second integer"""
    return num1 % num2

