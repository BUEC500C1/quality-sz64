import arabic2roman as a

def test_test():
    aNum = 59;
    rNum = a.arabic2roman(aNum);
    assert rNum == 'LIX';