import pytest
import sys, os
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# EOBlock

import playground

def test_find_minima():
    peaks = playground.core.find_dark_color([(7,4,2), (1,2,1), (5,3,5)])
    assert peaks == [(1,2,1)]

def test_empty():
    peaks = playground.core.find_dark_color([])
    assert peaks == []
