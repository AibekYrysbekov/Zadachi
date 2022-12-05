def f():
    a = float(input("Введите начальную сумму вклада: "))
    years = int(input("На сколько лет?: "))
    p = 10
    for i in range(years):
        a=a/100.0*p+a
    print('Количество денег за', years, ' лет составит', round(a,2), 'рублей')
f()