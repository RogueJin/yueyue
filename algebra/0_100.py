import random

max_num = 100
count = 20
operators = ["+", "-", "x", "/"]

while count > 0:
	totalnums = random.randint(2,4)
	result = random.randint(0, max_num)
	equation = str(result)
	
	for i in range(1, totalnums):
		num = random.randint(0, max_num)
		operator = operators[random.randint(0,1)]

		if operator == '+':
			result += num
		elif operator == '-':
			result -= num
			if result < 0:
				operator = "+"
				result += num * 2

		elif operator == '*':
			result *= num
		elif operator == '/':
			result /= num

		equation += operator
		equation += str(num)

	print "%s = " % (equation)
	count -= 1
