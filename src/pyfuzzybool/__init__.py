"""PyFuzzyBool
By Al Sweigart al@inventwithpython.com

Additional boolean values: KindaTrue, KindaFalse, VeryTrue, and VeryFalse. (This is a joke project.)"""

__version__ = '0.1.0'

import random

class _kindatrue:
    def __init__(self):
        raise Exception('Instantiating _kindatrue is not allowed, probably.')

class _kindafalse:
    def __init__(self):
        raise Exception('Instantiating _kindatrue is not allowed, probably.')

_KINDA_TRUE = 0
_KINDA_FALSE = 1
_VERY_TRUE = 2
_VERY_FALSE = 3
_TRUE = 4
_FALSE = 5

class fuzzybool:
    def __init__(self, value=None, **kwargs):
        if value is None:
            if kwargs.get('fuzzyValue') is None:
                self._fuzzyVal = _KINDA_FALSE
            else:
                fuzzyValue = kwargs.get('fuzzyValue')
                if not issubclass(type(fuzzyValue), str):
                    raise TypeError("fuzzyValue must be one of 'KindaTrue', 'KindaFalse', 'VeryTrue', 'VeryFalse', 'True', or 'False'.")
                else:
                    if fuzzyValue not in ('KindaTrue', 'KindaFalse', 'VeryTrue', 'VeryFalse', 'True', 'False'):
                        raise ValueError("fuzzyValue must be one of 'KindaTrue', 'KindaFalse', 'VeryTrue', 'VeryFalse', 'True', or 'False'.")
                    else:
                        if fuzzyValue == 'KindaTrue':
                            self._fuzzyVal = _KINDA_TRUE
                        elif fuzzyValue == 'KindaFalse':
                            self._fuzzyVal = _KINDA_FALSE
                        elif fuzzyValue == 'VeryTrue':
                            self._fuzzyVal = _VERY_TRUE
                        elif fuzzyValue == 'VeryFalse':
                            self._fuzzyVal = _VERY_FALSE
                        elif fuzzyValue == 'True':
                            self._fuzzyVal = _TRUE
                        elif fuzzyValue == 'False':
                            self._fuzzyVal = _FALSE


            return
        elif value is _kindatrue:
            self._fuzzyVal = _KINDA_TRUE
            return
        elif value is _kindafalse:
            self._fuzzyVal = _KINDA_FALSE
            return
        elif issubclass(type(value), type(self)):
            self._fuzzyVal = value._fuzzyVal
            return

        try:
            if 0.0 < float(value) < 1.0:
                if random.randint(0, 1):
                    self._fuzzyVal = _KINDA_TRUE
                else:
                    self._fuzzyVal = _KINDA_FALSE
            elif float(value) > 1.0:
                self._fuzzyVal = _VERY_TRUE
            elif float(value) < 0.0:
                self._fuzzyVal = _VERY_FALSE
            elif float(value) == 1.0:
                self._fuzzyVal = _TRUE
            elif float(value) == 0.0:
                self._fuzzyVal = _FALSE
            else:
                assert False
        except (ValueError, TypeError):
            if bool(value):
                self._fuzzyVal = _TRUE
            else:
                self._fuzzyVal = _FALSE


    def __str__(self):
        if self._fuzzyVal == _KINDA_TRUE:
            return 'KindaTrue'
        if self._fuzzyVal == _KINDA_FALSE:
            return 'KindaFalse'
        if self._fuzzyVal == _VERY_TRUE:
            return 'VeryTrue'
        if self._fuzzyVal == _VERY_FALSE:
            return 'VeryFalse'
        if self._fuzzyVal == _TRUE:
            return 'True'
        if self._fuzzyVal == _FALSE:
            return 'False'


    def __repr__(self):
        if self._fuzzyVal == _KINDA_TRUE:
            return "fuzzybool(fuzzyValue='KindaTrue')"
        elif self._fuzzyVal == _KINDA_FALSE:
            return "fuzzybool(fuzzyValue='KindaFalse')"
        elif self._fuzzyVal == _VERY_TRUE:
            return "fuzzybool(fuzzyValue='VeryTrue')"
        elif self._fuzzyVal == _VERY_FALSE:
            return "fuzzybool(fuzzyValue='VeryFalse')"
        elif self._fuzzyVal == _TRUE:
            return "fuzzybool(fuzzyValue='True')"
        elif self._fuzzyVal == _FALSE:
            return "fuzzybool(fuzzyValue='False')"


    def __eq__(self, other):
        # Handle if `other` is also a fuzzybool:
        if issubclass(type(other), type(self)):
            if (self._fuzzyVal == _KINDA_TRUE or self._fuzzyVal == _KINDA_FALSE) and (other._fuzzyVal == _KINDA_TRUE or other._fuzzyVal == _KINDA_FALSE):
                return True
            return self._fuzzyVal == other._fuzzyVal

        # Handle all other types for `other`:
        return self._fuzzyVal == fuzzybool(other)._fuzzyVal


    def __hash__(self):
        return self._fuzzyVal






# TODO: Write a PEP so that Python adopts these as keywords.
KindaTrue = fuzzybool(_kindatrue)
KindaFalse = fuzzybool(_kindafalse)
VeryTrue = fuzzybool(1.1)
VeryFalse = fuzzybool(-0.1)
