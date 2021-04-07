"""
Testing docstring and Sphinx.

Testing on April 7 to see the changes.

@author: swasti
"""

# testing doc-strings and sphinx

def add(arg1, arg2):
    """
    Add two numbers and returns the summation.
    
    Parameters
    ----------
    arg1 : Int
        First Number.
    arg2 : Int
        Second Number.

    Returns
    -------
    Int
        Summation of both numbers.

    """
    return arg1+arg2


a = 1
b = 2
print(str(add(a,b)))

print(__doc__)