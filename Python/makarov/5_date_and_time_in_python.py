# # Дата и время в Питоне

# +
# импортируем весь модуль
import datetime

# чтобы получить доступ к функции now(), сначала обратимся к модулю, потом к классу
print(datetime.datetime.now())

# +
# часто из модуля datetime удобнее импортировать только класс datetime
from datetime import datetime

# и обращаться непосредственно к нему
print(datetime.now())
# -

# поместим созданный с помощью функции now() объект datetime в переменную cur_dt
cur_dt = datetime.now()
print(cur_dt)

# с помощью соответствующих атрибутов выведем каждый из компонентов объекта по отдельности
print(cur_dt.year, cur_dt.month, cur_dt.day, cur_dt.hour, cur_dt.minute, cur_dt.second, cur_dt.microsecond)

# также можно посмотреть на день недели
# метод .weekday() начинает индекс недели с нуля, .isoweekday() - с единицы
print(cur_dt.weekday(), cur_dt.isoweekday())

# посмотрим на часовой пояс с помощью атрибута tzinfo
print(cur_dt.tzinfo)

# +
# для изменения часового пояса нужно импортировать модуль pytz
import pytz

# выведем текущее время в Москве
dt_moscow = datetime.now(pytz.timezone('Europe/Moscow'))
print(dt_moscow)
# -

# снова посмотрим на атрибут часового пояса
print(dt_moscow.tzinfo)

# получим timestamp текущего времени с помощью метода .timestamp()
timestamp = datetime.now().timestamp()

# выведем количество секунд, прошедшее с 01.01.1970 до исполнения кода
print(timestamp)

# вернем timestamp в прежний формат с помощью метода .fromtimestamp()
print(datetime.fromtimestamp(timestamp))

# передадим объекту datetime 20 февраля 1991 года
hb = datetime(1991, 2, 20)
print(hb)

# извлечем год с помощью атрибута year
print(hb.year)

# создадим timestamp
print(datetime.timestamp(hb))

# дана строка с датой 2 декабря 2007 года и временем 12 часов 30 минут и 45 секунд
str_to_dt = '2007-12-02 12:30:45'
type(str_to_dt)

# +
# преобразуем ее в datetime с помощью метода .strptime()
res_dt = datetime.strptime(str_to_dt, '%Y-%m-%d %H:%M:%S')

print(res_dt)
print(type(res_dt))
# -

# вначале создадим объект datetime и передадим ему 19 ноября 2002 года
dt_to_str = datetime(2002, 11, 19)
type(dt_to_str)

# +
# преобразуем объект в строку в формате "день недели, месяц число, год"
res_str = datetime.strftime(dt_to_str, '%A, %B %d, %Y')

print(res_str)
print(type(res_str))
# -

# .strftime() можно применять непосредственно к объекту datetime
dt_to_str.strftime('%A, %B %d, %Y')

# можно и так
datetime.now().strftime('%Y-%m-%d')

# а еще так
datetime.now().strftime('%c')

# сравним две даты публикации работ Эйнштейна
date1 = datetime(1905, 6, 30) # "К электродинамике движущихся тел"
date2 = datetime(1916, 5, 11) # Общая теория относительности

# большей считается более поздняя дата
date1 < date2

# обратное будет признано ложным
date1 > date2

# +
# если даты записаны в виде строки в формате ГГГГ.ММ.ДД,
# то мы можем их сравнивать, как если бы мы сравнивали объекты datetime

# вначале запишем даты в виде строки и сравним их
'2007-12-02' > '2002-11-19'
# -

# теперь в виде объекта datetime
datetime(2007, 12, 2) > datetime(2002, 11, 19)

# если из большей даты вычесть меньшую, то мы получим временной промежуток между датами
diff = date2 - date1
print(diff)

# при этом результат будет храниться в специальном объекте timedelta
type(diff)

# атрибут days позволяет посмотреть только дни
print(diff.days)

print(diff.years)

# +
# объект timedelta можно также создать вручную

# для этого вначале импортируем соответствующий класс
from datetime import timedelta

# а затем создадим объект timedelta продолжительностью 1 день
timedelta(days = 1)

# +
# смотрите, что получается,
# объединив объекты datetime и timedelta, мы можем "путешествовать во времени"

# допустим сейчас 1 января 2070 года
future = datetime(2070, 1, 1)
future

# +
# а мы хотим отправиться в 1 января 1900 года, т.е. на 170 лет назад

# сначала просто умножим 365 дней на 170
time_travel = timedelta(days = 365) * 170

# а потом переместимся из будущего в прошлое
past = future - time_travel

# к сожалению, мы немного "не долетим", потому что не учли високосные годы, в которых 366 дней
past
# -

# мы пролетели 62050 дней
365 * 170

# но мы уже умеем вычислять точное количество дней (с учетом високосных годов)
datetime(2070, 1, 1) - datetime(1900, 1, 1)

# +
# теперь снова совершим путешествие во времени, но на этот раз укажем правильное количество дней
time_travel = timedelta(days = 62092)

past = future - time_travel
past

# +
# иногда бывает удобно воспользоваться циклом while, чтобы создать перечень дат
# например, список праздничных новогодних дней в 2021 году

cur_date = datetime(2021, 1, 1)  # эту дату мы будем выводить
end_date = datetime(2021, 1, 10) # это граница (условие в цикле while)

# пока верно условие
while cur_date <= end_date:

  # выведем cur_date в формате "месяц число, год"
  print(cur_date.strftime('%b %d, %Y'))

  # прибавим к выводимой дате один день
  cur_date += timedelta(days = 1)

# +
# пусть дан список чисел в строковом формате, и мы хотим посчитать их сумму
# предположим, буква "а" попала в список случайно
numbers = ['5', '10', 'a', '15', '10']

# объявим переменную суммы
total = 0

# пройдемся по числам
for number in numbers:

  # попробуем прибавить число к переменной total
  try:
    total += int(number)

  # если же этого сделать не удастся
  except:
    # перейдем к следующему числу
    pass

# выведем сумму
total

# +
# напишем этот же код
total = 0

for number in numbers:
  try:
    total += int(number)
  except:
    # но выведем предупреждение, если число прибавить не удалось
    print(f'Элемент \'{number}\' обработать не удалось')

total
# -

# у нас есть данные по среднемесячной температуре в Нью-Йорке в 2002 году
import pandas as pd
temp = pd.read_csv('temperature.csv')
temp

# +
# предположим, проанализировав все форматы дат, мы выявили следующие шаблоны
formats = ['%Y-%m-%d', '%Y-%m-%-d', '%Y-%m']

# создадим счетчик для записей, которые не обработались
counter = 0

# пройдемся в цикле по столбцу Date
for d in temp.Date:

  # затем пройдемся по известным нам форматам
  for format in formats:

    # попробуем, применив каждый из форматов,
    # преобразовать строку с датой в объект datetime
    try:
      print(datetime.strptime(d, format))
      counter += 1

    # если что-то пошло не так
    except:
      # перейдем к следующему формату (второй цикл for) или записи (первый цикл for)
      pass

# посмотрим, сколько записей не обработалось
print('Не обработалось записей:', len(temp) - counter)
# -

# воспользуемся решением "из коробки" библиотеки Pandas
# передадим функции read_csv() параметр parse_dates
temp_parsed = pd.read_csv('temperature.csv', index_col = 'Date', parse_dates = True)
temp_parsed

# индекс превратился в объект datetime
type(temp_parsed.index)


