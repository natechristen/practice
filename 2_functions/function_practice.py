# here are two sample 2_functions. try changing the values passed
# through the simple_addition function

def example():
    # this code is inside the function
    print('Here are the results from the function called "example"')
    z = 3 + 9
    print(z)


# this code is outside the function
example()


# How do you pass variables through a function?
def simple_addition(num1, num2):
    print('Here are the results from the function called "sample_addition"')
    answer = num1 + num2
    print('num1 is', num1)
    print('num2 is', num2)
    print(num1, " + ", num2, " = ", answer)


simple_addition(5, 4)
