#!/usr/bin/env python2
"""
Good Bye!
"""


def goodbye(to=None):
    '''
    Say goodbye to `to`.

    >>> goodbye()
    'bye.'
    >>> goodbye('Fred')
    'Goodbye, Fred.'
    >>> goodbye(to='Autumn')
    'Goodbye, Autumn.'
    '''
    message = "bye."
    if to:
        message = "Goodbye, {}.".format(to)
    return message


if __name__ == "__main__":
    goodbye()
