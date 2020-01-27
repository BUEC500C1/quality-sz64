import arabic2roman as a

def test_valid():
    aNum = 59;
    rNum = a.arabic2roman(aNum);
    assert rNum == 'LIX';
	
def test_invalid():
    aNum = 'string';
    rNum = a.arabic2roman(aNum);
    assert rNum == 'Error';