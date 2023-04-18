from python-package import myModule

def test_top_n():
    """
    testing top_n func

    """
    assert myModule.top_n([8,7,5,4,6,], 3) == [8,7,6], 'incorrect'
    assert myModule.top_n([12,4, 6, 8, 9 ], 3) == [12, 9, 8], 'incorrect'
