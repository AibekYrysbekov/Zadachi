def f():
    total = 0
    days = int(input('Введите измеренные дни: '))
    for i in range(days):
        temperature = float(input('Температура: '))
        if temperature >-300:
            total += temperature
        else:
            print('Реальная температура не может быть ниже -300!')
            break
    print('Среднее температура воздуха:',round(total/days,1))
f()