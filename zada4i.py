#1
'''
list_1 = ['name', 'age', '1', '19']

a = list_1[:len(list_1)//2]
b = list_1[len(list_1)//2:]
a.reverse()
b.reverse()
print(a + b)

#2

def half_list(list_1):
    half = len(list_1) // 2
    return list_1[:half][::-1], list_1[half:][::-1]

print(half_list(list_1))



def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(10))
print(data)

#3

def sum_chis():
    a = int(input('-> '))
    b = int(input('-> '))
    c = a + b
    return c



def raz_chis():
    x = int(input('-> '))
    y = int(input('-> '))
    f = x - y
    return f



def abc():
    print (sum_chis(), raz_chis())

abc()



def file_name():
    a = input('Имя файла: ')
    with open(f'{a}', 'w') as f:
        f.write('kbbbkbckjbskb')
        return f'{a}'
n = file_name()
print(n)



d1 = {1: 2, 2: 3}
d2 = {4: 5, 6: 7}

def dist_in_dict(a, b):
    a.update(b)
    print(a)
dist_in_dict(d1, d2)


print((lambda x: d1) (d1.update(d2)))



def order(order):
    with open('menu.txt', 'w') as f:
        f.write(order)

order(input('-> '))



def first():
    return 'я главная функция'
def second(a):
    print('я вложенная функция')
    print(a)

second(first())



a = {1: 2, 3: 4, 5: 6}
def dictionary_tuple(a):
    print(tuple(a))
    print(tuple(a.values()))
dictionary_tuple(a)
  

def create_file(file_name):
    with open(f'{file_name}', 'w') as file:
        pass

create_file(input('-> '))

'''

