# ## # ## # ## #
# Functions and Variable scope

# def keyword makes a function
def greet(name):
    # indentation block (scope of the function)
    print('Hello, ' + name) # string concatenation

    #format string (like string interpolation)
    s = 'spam'
    print(f'Hello, {name} {s} {s}')

    # format template
    print('Hello, {} {} {}'.format(name, s , name))

# invocation of the function
greet('April')
