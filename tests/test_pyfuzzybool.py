from __future__ import division, print_function
import pytest
from pyfuzzybool import *


def test_names():
    KindaTrue
    KindaFalse
    VeryTrue
    VeryFalse
    fuzzybool

def test_init():
    assert fuzzybool() == KindaFalse
    assert fuzzybool(1.1) == VeryTrue
    assert fuzzybool(-0.1) == VeryFalse

    # Truthy values:
    assert fuzzybool(1) == True
    assert fuzzybool(True) == True
    assert fuzzybool('hello') == True
    assert fuzzybool(['hello']) == True
    assert fuzzybool(('cat', 'dog')) == True
    assert fuzzybool({'key': 'value'}) == True

    # Falsey values:
    assert fuzzybool(0) == False
    assert fuzzybool(False) == False
    assert fuzzybool('') == False
    assert fuzzybool([]) == False
    assert fuzzybool(()) == False
    assert fuzzybool({}) == False

    # fuzzyValue parameter:
    assert fuzzybool(fuzzyValue='KindaTrue')._fuzzyVal == KindaTrue._fuzzyVal
    assert fuzzybool(fuzzyValue='KindaFalse')._fuzzyVal == KindaFalse._fuzzyVal
    assert fuzzybool(fuzzyValue='VeryTrue')._fuzzyVal == VeryTrue._fuzzyVal
    assert fuzzybool(fuzzyValue='VeryFalse')._fuzzyVal == VeryFalse._fuzzyVal
    assert fuzzybool(fuzzyValue='True')._fuzzyVal == 4  # Using the enum int value directly here.
    assert fuzzybool(fuzzyValue='False')._fuzzyVal == 5  # Using the enum int value directly here.


def test_str():
    assert str(KindaTrue) == 'KindaTrue'
    assert str(KindaFalse) == 'KindaFalse'
    assert str(VeryTrue) == 'VeryTrue'
    assert str(VeryFalse) == 'VeryFalse'

    assert str(fuzzybool(1)) == 'True'
    assert str(fuzzybool(0)) == 'False'


def test_repr():
    assert repr(KindaTrue) == "fuzzybool(fuzzyValue='KindaTrue')"
    assert repr(KindaFalse) == "fuzzybool(fuzzyValue='KindaFalse')"
    assert repr(VeryTrue) == "fuzzybool(fuzzyValue='VeryTrue')"
    assert repr(VeryFalse) == "fuzzybool(fuzzyValue='VeryFalse')"
    assert repr(fuzzybool(1)) == "fuzzybool(fuzzyValue='True')"
    assert repr(fuzzybool(0)) == "fuzzybool(fuzzyValue='False')"





if __name__ == "__main__":
    pytest.main()

