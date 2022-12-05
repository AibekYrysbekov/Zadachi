# Банкомат
# Напишите код банкомата, который принимает цифру, выдает деньги с номиналом 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.

def f(nominal):
    bankomat = {5000: 10, 2000: 20, 1000: 100, 500: 100, 200: 100, 100: 100, 50: 100, 20: 100, 10: 100, 5: 100, 3: 100, 1: 100}
    result = {5000: 0, 2000: 0,  1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 3: 0, 1: 0}
    for k, v in bankomat.items():
        if nominal == 0:
            print("Введите сумму больше '0'")
            break
        while bankomat[k] > 0 and nominal >= k:
            bankomat[k] = bankomat[k] - 1
            result[k] += 1
            nominal -= k
            if nominal == 0:
                print(f'''5000 - {result[5000]}
    2000 - {result[2000]}
    1000 - {result[1000]}
    500 - {result[500]}
    100 - {result[100]}
    50 - {result[50]}
    20 - {result[20]}
    10 - {result[10]}
    5 - {result[5]}
    3 - {result[3]}
    1 - {result[1]}''')


nominal = int(input('Введите сумму: '))
f(nominal)
bankomat = {5000:10, 2000:20, 1000: 100, 500:100, 200:100, 100:100, 50:100, 20:100, 10:100, 5:100, 3:100, 1:100}
summa = []
for k, v in bankomat.items():
    summa.append(k * v)
    if sum(summa) < nominal:
        print('Сумма превышает лимит')
        break