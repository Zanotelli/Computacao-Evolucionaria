import pytest
import * from evolutionary

def test_mutate_offspring():
    x = [5, 7, 1 , 2, 0, 3, 4, 6]
    assert fitness_nq(X) == 8