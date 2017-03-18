import random

count = 10

while count > 0:
	print "%d + %d = " % (random.randint(0, 10), random.randint(0, 10))
	count -= 1