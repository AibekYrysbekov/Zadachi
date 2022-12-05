def f():
	dict_one = {'a':1, 'b':2, 'c':3}
	dict_two = {'d':4, 'e':5, 'f':6}
	dict_three = {'g':7, 'h':8, 'i':9}
	dict_four = {}

	dict_tuple = dict_one, dict_two, dict_three
	print(dict_tuple)

	for i in dict_tuple:
    		print(i)
    		dict_four.update(i)

	print(dict_four)
f()