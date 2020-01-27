import arabic2roman as a

def test_valid():								# Checks values within the valid range
	assert a.arabic2roman(1) == 'I';
	assert a.arabic2roman(4) == 'IV';
	assert a.arabic2roman(9) == 'IX';
	assert a.arabic2roman(59) == 'LIX';
	assert a.arabic2roman(94) == 'XCIV';
	assert a.arabic2roman(495) == 'CDXCV';
	assert a.arabic2roman(999) == 'CMXCIX';
	assert a.arabic2roman(1010) == 'MX';
	assert a.arabic2roman(1489) == 'MCDLXXXIX';
	assert a.arabic2roman(3999) == 'MMMCMXCIX';
	
def test_invalid():
	assert a.arabic2roman('string') == 'Error'; # Only integers are valid
	assert a.arabic2roman(4.2) == 'Error';		# Floating point is invalid
	assert a.arabic2roman(-1) == 'Error';		# Current function only works with values 1 to 3999
	assert a.arabic2roman(0) == 'Error';
	assert a.arabic2roman(4000) == 'Error';