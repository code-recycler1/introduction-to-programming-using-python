# Function that prints double the parameter value
def show_double(value):
    print(value * 2)


# Function that returns double the parameter value
def double(value):
    return value * 2


# Function that returns the larger of two numbers
def maximum(number1, number2):
    if number1 > number2:
        return number1
    return number2


# Function that checks if the square of one number is smaller than another
def square_is_smaller(number1, number2):
    return number1 ** 2 < number2


# Function that returns the type of triangle based on three sides
def triangle_type(a, b, c):
    if a == b and b == c:
        return 'equilateral triangle'
    elif c ** 2 == a ** 2 + b ** 2:
        return 'right triangle'
    else:
        return 'other triangle'


