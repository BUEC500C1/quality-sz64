def arabic2roman(aNum):
	if (isinstance(aNum, int) & (0 < aNum < 4000)):
		aNums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
		rNums = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
		rNum = '';
		i = 0;
		while aNum > 0:
			for _ in range(aNum//aNums[i]):
				rNum += rNums[i];
				aNum -= aNums[i];
			i += 1;
		return rNum;
	else:
		return 'Error';