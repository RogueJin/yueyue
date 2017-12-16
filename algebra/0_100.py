import random

max_num = 100
count = 20
operators = ["+", "-", "x", "/"]

while count > 0:
	nums = random.randint(2,4)
	equation = str(random.randint(0, max_num))

	for i in range(1, nums):
		operator = operators[random.randint(0,1)]
		equation += operator
		equation += str(random.randint(0, max_num))

	print "%s = " % (equation)
	count -= 1
