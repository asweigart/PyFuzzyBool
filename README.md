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

Contribute
----------

If you'd like to contribute to PyFuzzyBool, check out https://github.com/asweigart/pyfuzzybool
