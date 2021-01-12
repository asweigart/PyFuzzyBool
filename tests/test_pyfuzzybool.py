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
    assert fuzzybool(fuzzyValue='False')._fuzzyVal == 1  # Using the enum int value directly here.


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


def test_comparison():
    assert VeryTrue == VeryTrue
    assert VeryFalse == VeryFalse
    assert KindaTrue == KindaFalse
    assert KindaFalse == KindaTrue
    assert KindaTrue != True
    assert KindaTrue != False
    assert KindaFalse != True
    assert KindaFalse != False
    assert VeryTrue == True
    assert VeryTrue != False
    assert VeryFalse == False
    assert VeryFalse != True
    assert VeryTrue != KindaTrue
    assert VeryTrue != KindaFalse
    assert VeryFalse != KindaTrue
    assert VeryFalse != KindaFalse

    assert VeryTrue == fuzzybool(fuzzyValue='VeryTrue')
    assert VeryFalse == fuzzybool(fuzzyValue='VeryFalse')
    assert KindaTrue == fuzzybool(fuzzyValue='KindaFalse')
    assert KindaFalse == fuzzybool(fuzzyValue='KindaTrue')
    assert KindaTrue != True
    assert KindaTrue != False
    assert KindaFalse != True
    assert KindaFalse != False
    assert VeryTrue == True
    assert VeryTrue != False
    assert VeryFalse == False
    assert VeryFalse != True
    assert VeryTrue != fuzzybool(fuzzyValue='KindaTrue')
    assert VeryTrue != fuzzybool(fuzzyValue='KindaFalse')
    assert VeryFalse != fuzzybool(fuzzyValue='KindaTrue')
    assert VeryFalse != fuzzybool(fuzzyValue='KindaFalse')

    assert fuzzybool(fuzzyValue='VeryTrue') == VeryTrue
    assert fuzzybool(fuzzyValue='VeryFalse') == VeryFalse
    assert fuzzybool(fuzzyValue='KindaFalse') == KindaTrue
    assert fuzzybool(fuzzyValue='KindaTrue') == KindaFalse
    assert True != KindaTrue
    assert False != KindaTrue
    assert True != KindaFalse
    assert False != KindaFalse
    assert True == VeryTrue
    assert False != VeryTrue
    assert False == VeryFalse
    assert True != VeryFalse
    assert fuzzybool(fuzzyValue='KindaTrue') != VeryTrue
    assert fuzzybool(fuzzyValue='KindaFalse') != VeryTrue
    assert fuzzybool(fuzzyValue='KindaTrue') != VeryFalse
    assert fuzzybool(fuzzyValue='KindaFalse') != VeryFalse

    assert not (KindaTrue < KindaFalse)
    assert not (KindaTrue > KindaFalse)
    assert not (KindaFalse < KindaTrue)
    assert not (KindaFalse > KindaTrue)


def test_float():
    assert float(fuzzybool(fuzzyValue='True')) == 1.0
    assert float(fuzzybool(fuzzyValue='False')) == 0.0

    for i in range(100):
        assert 0.0 < float(KindaFalse) < 1.0
        assert 0.0 < float(KindaTrue) < 1.0
        assert 0.0 < float(fuzzybool(fuzzyValue='KindaFalse')) < 1.0
        assert 0.0 < float(fuzzybool(fuzzyValue='KindaTrue')) < 1.0
        assert float(fuzzybool(fuzzyValue='VeryTrue')) > 1.0
        assert float(fuzzybool(fuzzyValue='VeryFalse')) < 0.0


if __name__ == "__main__":
    pytest.main()

