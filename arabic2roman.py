def arabic2roman(aNum):
    aNums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    rNums = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
    rNum = '';
    i = 0;
    while aNum > 0:
        for _ in range(aNum//aNums[i])
            rNum += rNums[i];
            aNum -= val[i];
        i += 1;
    return rNum;

# while(True):
	# print('Enter a Arabic Number: ');
	# aNum = input();
    # rNum = arabic2roman(aNum);
	# print(rNum);
