def f():
	a = []
	plus = []
	minus = []

	for k in range(5):
		num = int(input('Введите числа: '))
		a.append(num)

	for i in a:
		if i>=0:
			plus.append(i)
		else:
			minus.append(i)

	print(f'Положительные: {plus}')
	print(f'Отрицательные: {minus}')
f()