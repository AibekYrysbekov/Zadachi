#1. Напишите программу, которая принимает имя файла и выводит его расширение.
# Если расширение у файла определить невозможно, выбросите исключение.

def get_extension(filename):
    filename_parts = filename.split('.')
    if len(filename_parts) < 2:  # filename has no dots
        raise ValueError('the file has no extension')
    first, *middle, last = filename_parts
    if not last or not first and not middle:
        # example filenames: .filename, filename., file.name.
        raise ValueError('the file has no extension')
    return filename_parts[-1]
print(get_extension(input("Имя файла: ")))

#2. Напишите функцию, которая принимает год и определяет, является ли год с данным номером високосным.
# Если год является високосным, то возвращает «YES», иначе возвращает «NO».Год является високосным, если его номер кратен 4,
# но не кратен 100, или если он кратен 400.

def is_year_leap(year):
     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_year_leap(2000))

#3. Напишите функцию, которая принимает возраст собаки и нужно вычислить, возраст собаки в
# человеческих годах.(В течение первых двух лет собачий год равен 10.5 человеческим годам.
# После этого каждый год собаки равен 4 человеческим годам).
a = 10.5
b = 4
def dog_years(age):
    if 0< age <= 2:
        return age*10.5
    else: print(2 * 10.5 + (age - 2) * 4)
print(dog_years(int(input('Bведите возраст собаки: '))))

# #4.  Напишите алгоритм, определяющий, является ли число n счастливым.
# Счастливое число — это число, определяемое следующим процессом:
# Начиная с любого положительного целого числа, замените число суммой квадратов его цифр.
# Повторяйте процесс до тех пор, пока число не станет равным 1 (где оно и останется),
# или пока он не будет бесконечно повторяться в цикле , который не включает 1.
# Те числа, для которых этот процесс заканчивается на 1 , счастливы.
# Возврат true , если n это счастливое число, а false если нет .


def chislo(n):
    a = list(map(int, str(n)))
    res = sum([i**2 for i in a])
    if res == 1:
        print('это счастливое число')
    elif len([i for i in a if i != 0]) == 1:
        print('это не счастливое число')
    else:
        chislo(res)
chislo(input())


# 5. Строка считается заглавной, если каждое слово в строке либо (а) пишется с заглавной буквы
# (то есть только первая буква слова в верхнем регистре),
# либо (б) считается исключением и полностью помещается в строчными буквами, если только это не первое слово,
# которое всегда пишется с большой буквы.
# Напишите функцию, которая преобразует строку в заглавный регистр, учитывая необязательный список исключений
# (второстепенные слова).
# Список второстепенных слов будет представлен в виде строки, где каждое слово отделено пробелом.
# Ваша функция должна игнорировать регистр строки второстепенных слов — она должна вести себя так же,
# даже если регистр строки второстепенных слов изменен.
# Первый аргумент (обязательный): исходная строка для преобразования.
# Второй аргумент (необязательный): список второстепенных слов, разделенных пробелами,
# которые всегда должны быть строчными, за исключением первого слова в строке

def titlle_case():
    a = ('a clash of KINGS', 'a an the of')
    b = str.title(a[0])
    return b
print(titlle_case())

def titlle_case1():
    x = ('THE WIND IN THE WILLOWS', 'The In')
    y = str.title(x[0])
    return y
print(titlle_case1())

def titlle_case2():
    x = ('the quick brown fox')
    y = str.title(x)
    return y
print(titlle_case2())

#6. Напишите функцию to_weird_case, которая принимает строку и возвращает ту же строку,
# в которой все символы с четным индексом в каждом слове отображаются в верхнем регистре,
# а все символы с нечетным индексом в каждом слове — в нижнем регистре.
# Только что объясненная индексация основана на нуле, поэтому нулевой индекс четный,
# поэтому этот символ должен быть в верхнем регистре, и вам нужно начинать заново для каждого слова.
# Передаваемая строка будет состоять только из букв алфавита и пробелов (' ').
# Пробелы будут присутствовать только в том случае, если слов несколько.
# Слова будут разделены одним пробелом (' ').

def word_case(string):
    num = 0
    new_word = []
    for i in string:
        if num % 2 == 0:
            num += 1
            new_word.append(i.upper())
        else:
            num += 1
            new_word.append(i.lower())
    print(''.join(new_word))
word_case(input())


#7. ваша задача — создать функцию, которая превращает строку в мексиканскую волну.
# Вам будет передана строка, и вы должны вернуть эту строку в виде массива,
# где заглавная буква означает стоящего человека (https://ru.wikipedia.org/wiki/Волна_(стадион).
# Правила:
# 1. Строка ввода всегда будет строчной, но может быть и пустой.
# 2. Если символ в строке является пробелом, пропустите его, как если бы это было пустое место.
def Mexican_wave():
    s = input('-> ')
    new = []
    for i, val in enumerate(s[:]):
        up = s[i].upper()
        c = s[:i] + up + s[i+1:]
        new.append(c)
    print(new)
Mexican_wave()
