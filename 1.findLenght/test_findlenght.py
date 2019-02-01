import findlenght
def test_assertTrue():
    assert True


def test_listreturn6():
    #arrange
    array = [1,2,3,4,5,6]
    excepted = 6
    #act
    actual = findlenght.len(array)
    #assert
    assert excepted == actual