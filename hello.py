#!/usr/bin/env python3

def say_hello(name="World"):
    """
    Returns a hello string with the supplied name, or 'World' if no name given.

    >>> say_hello()
    'Hello, World!'
    >>> say_hello("Bob")
    'Hello, Bob!'
    """
    return "Hello, {}!".format(name)

print(say_hello())
