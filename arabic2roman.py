def arabic2roman(aNum):
	if isinstance(aNum, int): # Only integer types are valid
		if (0 < aNum < 4000): # Only integers in this range valid, or add a system to incorporate bars over characters
			aNums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
			rNums = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
			rNum = '';
			i = 0;
			while aNum > 0: # Splits number up into the roman numerals from larger values to smaller ones
				for _ in range(aNum//aNums[i]):
					rNum += rNums[i];
					aNum -= aNums[i];
				i += 1;
			return rNum;
		else:
			return 'Error';
	else:
		return 'Error';