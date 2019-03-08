import findlenght

def test_assertTrue(): #Environment test
    assert True


def test_listreturn6():
    #arrange
    array = [1,2,3,4,5,6]
    excepted = 6
    #act
    actual = findlenght.lenght(array)
    #assert
    assert excepted == actual
