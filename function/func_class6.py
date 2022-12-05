def f():
	steps = [4, 5, 6, 7, 8, 9, 0]
	print(steps)
	num = int(input('Введите число -> '))

	if 0 > num:
		num = abs(num)
	for i in range(num):
		steps.append(steps.pop(0))
		print(steps)
	else:
		for i in range(num):
			steps.insert(0, steps.pop())
		print(steps)
f()