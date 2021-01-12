PyFuzzyBool
======

Additional boolean values: KindaTrue, KindaFalse, VeryTrue, and VeryFalse. (This is a joke project.)

Installation
------------

To install with pip, run:

    pip install pyfuzzybool

Quickstart Guide
----------------

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
