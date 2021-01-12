PyFuzzyBool
======

Additional boolean values: KindaTrue, KindaFalse, VeryTrue, and VeryFalse. (This is a joke project.)

Installation
------------

To install with pip, run:

    pip install pyfuzzybool

Quickstart Guide
----------------

In the Python language, the bool data type is a subclass of integers. The values `True` and `False` are literally the same as the integer values `1` and `0`: you can use them any way you use integers: `True + True + False + True` evaluates to `3` and `'Hello[True]'` evaluates to `'e'`.

There is also a concept of "truthy" and "falsey" values in Python: `0`, `0.0`, blank strings, empty lists/dictionaries/tuples, and others are "falsey" values; when passed to `bool()` they will evaluate to the bool value `False`. All other values are "truthy" and when passed to `bool()` will evaluate to `True`.

Similarly, `fuzzybool(1)` and `fuzzybool(0)` will evaluate to `True` and `False`, but passing a float or int larger than `1.0` evaluates to `VeryTrue`, while passing a value less than `0.0` evaluates to `VeryFalse`. Passing a value between `0.0` and `1.0` will evaluate to `KindaTrue` half the time and `KindaFalse` the other time.

Here's some examples in the interactive shell:

    >>> from pyfuzzybool import *
    >>> KindaTrue == KindaFalse
    True
    >>> KindaTrue == True
    False
    >>> VeryTrue == True
    True
    >>> VeryFalse == False
    True
    >>> KindaFalse == False
    False
    >>> fuzzybool(1)
    fuzzybool(True)
    >>> fuzzybool(0.9)
    KindaTrue
    >>> fuzzybool(0)
    fuzzybool(False)
    >>> fuzzybool(-1)
    VeryFalse
    >>> fuzzybool(1.1)
    VeryTrue
    >>> fuzzybool()
    KindaFalse
    >>> KindaFalse < True
    True
    >>> KindaFalse > False
    True
    >>> KindaFalse <= KindaTrue
    True

I think a lot of these can be changed. Should `KindaTrue == True` evaluate to `True`? Or should it evaluate to `KindaTrue`? Or evaluate half the time to `KindaTrue` and the other half `KindaFalse`?

This project is a joke, but this opens up a lot of issues to think about (if you have nothing better to do). After all, mathematics is just a bunch of made up, arbitrary rules about how to operate on abstract symbols. Math just happens to turn out to be [unreasonably effective in science](https://en.wikipedia.org/wiki/The_Unreasonable_Effectiveness_of_Mathematics_in_the_Natural_Sciences).

Contribute
----------

If you'd like to contribute to PyFuzzyBool, check out https://github.com/asweigart/pyfuzzybool
