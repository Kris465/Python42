# Форматирование строк

1. Оператор % (старый стиль):

```python
   name = "Alice"
   age = 30
   formatted_string = "Name: %s, Age: %d" % (name, age)
```

2. Метод .format():
```python
   name = "Alice"
   age = 30
   formatted_string = "Name: {}, Age: {}".format(name, age)
```
3. f-строки (форматированные строковые литералы) (начиная с Python 3.6):

```python
   name = "Alice"
   age = 30
   formatted_string = f"Name: {name}, Age: {age}"
```

4. Метод str.format_map():

```python
   data = {'name': 'Alice', 'age': 30}
   formatted_string = "Name: {name}, Age: {age}".format_map(data)
```
5. Шаблоны строк с использованием модуля string:
```python
   from string import Template
   template = Template("Name: $name, Age: $age")
   formatted_string = template.substitute(name="Alice", age=30)
```

## О каждом подробнее

### Оператор % (старый стиль)

    Оператор % в Python, также известный как "старый стиль" форматирования строк, используется для подстановки значений в строки. Этот метод был популярен до появления метода .format() и f-строк (форматированных строковых литералов) в Python 3.6. Несмотря на то что он считается устаревшим, оператор % все еще поддерживается и может быть полезен в некоторых ситуациях.

▎Основы использования оператора %

Оператор % позволяет вставлять значения в строку, используя специальные символы формата. Основные символы формата включают:

• %s — строка

• %d — целое число

• %f — число с плавающей запятой

• %x — шестнадцатеричное число (маленькие буквы)

• %X — шестнадцатеричное число (большие буквы)

▎Примеры использования

▎1. Форматирование строк

```python
name = "Alice"
age = 30

# Используем оператор % для форматирования строки
formatted_string = "Name: %s, Age: %d" % (name, age)
print(formatted_string)  # Вывод: Name: Alice, Age: 30
```

В этом примере мы используем %s для подстановки строки и %d для подстановки целого числа.

▎2. Форматирование чисел с плавающей запятой

```python
price = 19.99
formatted_string = "Price: $%.2f" % price
print(formatted_string)  # Вывод: Price: $19.99
```
Здесь мы используем %.2f, чтобы отобразить число с плавающей запятой с двумя знаками после запятой.

▎3. Шестнадцатеричное форматирование

```python
number = 255
formatted_string = "Hexadecimal: %x" % number
print(formatted_string)  # Вывод: Hexadecimal: ff
```
В этом примере мы используем %x, чтобы представить число в шестнадцатеричном формате.

▎Дополнительные возможности

▎1. Выравнивание и ширина

Вы можете задать ширину поля и выравнивание для чисел и строк.

```python
name = "Bob"
age = 25

# Выравнивание по правому краю с шириной 10 символов
formatted_string = "|%10s|%5d|" % (name, age)
print(formatted_string)  # Вывод: |       Bob|   25|
```

В этом примере |%10s|%5d| означает, что строка будет занимать 10 символов, а число — 5 символов.

▎2. Заполнение пробелами или нулями

Вы также можете использовать заполнение для чисел.

```python
number = 42

# Заполнение нулями до ширины 5
formatted_string = "Number: %05d" % number
print(formatted_string)  # Вывод: Number: 00042
```

Здесь 05d означает, что число будет заполнено нулями до ширины 5.

▎Словари и кортежи

Вы можете использовать словари для подстановки значений.

```python
data = {
    'name': 'Charlie',
    'age': 35
}

formatted_string = "Name: %(name)s, Age: %(age)d" % data
print(formatted_string)  # Вывод: Name: Charlie, Age: 35
```
### Метод .format()

    Метод .format() в Python — это один из способов форматирования строк, который позволяет вставлять значения в строки, используя фигурные скобки {} как маркеры для подстановки. Этот метод был введен в Python 2.7 и стал стандартом в Python 3.x, предлагая более гибкий и мощный способ форматирования по сравнению с оператором %.

▎Основы использования метода .format()

Метод .format() позволяет вам вставлять переменные и выражения в строку, а также управлять их порядком, форматированием и другими аспектами.

▎1. Простейшее использование

```python
name = "Alice"
age = 30

formatted_string = "Name: {}, Age: {}".format(name, age)
print(formatted_string)  # Вывод: Name: Alice, Age: 30
```

В этом примере {} служат местозаполнителями для значений переменных name и age.

▎2. Позиционные аргументы

Вы можете использовать позиционные аргументы для управления порядком вставляемых значений.

```python
formatted_string = "Age: {1}, Name: {0}".format(name, age)
print(formatted_string)  # Вывод: Age: 30, Name: Alice
```
Здесь {1} соответствует второму аргументу (возраст), а {0} — первому (имя).

▎3. Именованные аргументы

Метод .format() также поддерживает именованные аргументы.

```python
formatted_string = "Name: {name}, Age: {age}".format(name="Bob", age=25)
print(formatted_string)  # Вывод: Name: Bob, Age: 25
```
В этом случае вы можете явно указать имена переменных, что делает код более читаемым.

▎4. Форматирование чисел

Вы можете использовать форматирование для чисел, чтобы контролировать количество знаков после запятой и другие параметры.

```python
pi = 3.14159
formatted_string = "Pi rounded to two decimal places: {:.2f}".format(pi)
print(formatted_string)  # Вывод: Pi rounded to two decimal places: 3.14
```

Здесь {:.2f} означает, что число будет отформатировано с двумя знаками после запятой.

▎5. Выравнивание и ширина

Метод .format() позволяет задавать ширину поля и выравнивание значений.

```python
name = "Charlie"
age = 35

formatted_string = "|{:>10}|{:^5}|".format(name, age)
print(formatted_string)  # Вывод: |   Charlie| 35  |
```

В этом примере {:>10} выравнивает имя по правому краю в поле шириной 10 символов, а {:^5} выравнивает возраст по центру в поле шириной 5 символов.

▎6. Заполнение пробелами или символами

Вы можете использовать заполнение для чисел и строк.

```python
number = 42

# Заполнение нулями до ширины 5
formatted_string = "Number: {:05}".format(number)
print(formatted_string)  # Вывод: Number: 00042
```

Здесь {:05} означает, что число будет заполнено нулями до ширины 5.

▎7. Форматирование дат

Метод .format() также можно использовать для форматирования дат.

```python
from datetime import datetime

now = datetime.now()
formatted_string = "Current date and time: {:%Y-%m-%d %H:%M:%S}".format(now)
print(formatted_string)  # Вывод: Current date and time: YYYY-MM-DD HH:MM:SS
```

Здесь используется специальный синтаксис для форматирования даты и времени.

### f-строки (форматированные строковые литералы) (начиная с Python 3.6)

    f-строки (форматированные строковые литералы) были введены в Python 3.6 и представляют собой удобный и эффективный способ форматирования строк. Они позволяют вставлять значения переменных непосредственно в строку, используя фигурные скобки {}. Это делает код более читаемым и сокращает необходимость в вызовах методов форматирования.

▎Основы f-строк

Чтобы создать f-строку, просто добавьте букву f или F перед начальной кавычкой строки. Внутри строки вы можете использовать фигурные скобки для вставки выражений и переменных.

▎Пример 1: Простое использование

```python
name = "Alice"
age = 30

formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)  # Вывод: Name: Alice, Age: 30
```

В этом примере значения переменных name и age вставляются прямо в строку.

▎Пример 2: Вставка выражений

Вы можете вставлять не только переменные, но и любые выражения внутри фигурных скобок.

```python
a = 5
b = 10

formatted_string = f"The sum of {a} and {b} is {a + b}."
print(formatted_string)  # Вывод: The sum of 5 and 10 is 15.
```

Здесь результат вычисления a + b также вставляется в строку.

▎Пример 3: Форматирование чисел

f-строки поддерживают форматирование чисел так же, как и метод .format().

```python
pi = 3.14159
formatted_string = f"Pi rounded to two decimal places: {pi:.2f}"
print(formatted_string)  # Вывод: Pi rounded to two decimal places: 3.14
```
Здесь {pi:.2f} означает, что значение pi будет отформатировано с двумя знаками после запятой.

▎Пример 4: Выравнивание и ширина

Вы также можете управлять выравниванием и шириной полей.

```python
name = "Charlie"
age = 35

formatted_string = f"|{name:>10}|{age:^5}|"
print(formatted_string)  # Вывод: |   Charlie| 35  |
```

В этом примере {:>10} выравнивает имя по правому краю в поле шириной 10 символов, а {:^5} выравнивает возраст по центру в поле шириной 5 символов.

▎Пример 5: Вложенные выражения

Вы можете использовать вложенные выражения в f-строках.
```python
value = 10
formatted_string = f"The value doubled is {value * 2} and tripled is {value * 3}."
print(formatted_string)  # Вывод: The value doubled is 20 and tripled is 30.
```
▎Пример 6: Использование методов и свойств

Вы можете вызывать методы и свойства объектов внутри f-строк.

```python
name = "alice"
formatted_string = f"Capitalized name: {name.capitalize()}"
print(formatted_string)  # Вывод: Capitalized name: Alice
```
### Метод str.format_map()

    Метод str.format_map() в Python является удобным способом форматирования строк, который позволяет использовать словари для подстановки значений в строку. Этот метод работает аналогично методу str.format(), но предоставляет более удобный способ работы с данными, хранящимися в виде словарей.

▎Основы метода str.format_map()

Метод format_map() принимает один аргумент — словарь (или любой объект, поддерживающий протокол отображения), и использует его для замены плейсхолдеров в строке.

▎Синтаксис

```python
str.format_map(mapping)
```

где mapping — это словарь, содержащий значения для подстановки.

▎Пример 1: Основное использование

```python
data = {'name': 'Alice', 'age': 30}
formatted_string = "Name: {name}, Age: {age}".format_map(data)
print(formatted_string)  # Вывод: Name: Alice, Age: 30
```

В этом примере мы создали словарь data и использовали его для форматирования строки.

▎Пример 2: Использование с вложенными словарями

Вы также можете использовать вложенные словари для доступа к значениям.

```python
data = {
    'person': {
        'name': 'Bob',
        'age': 25
    }
}
formatted_string = "Name: {person[name]}, Age: {person[age]}".format_map(data)
print(formatted_string)  # Вывод: Name: Bob, Age: 25
```

Здесь мы обращаемся к значениям внутри вложенного словаря person.

▎Пример 3: Обработка отсутствующих ключей

Если вы попытаетесь получить доступ к отсутствующему ключу, метод format_map() вызовет исключение KeyError. Чтобы избежать этого, можно использовать класс collections.defaultdict или реализовать свой собственный механизм обработки отсутствующих значений.

▎Пример с использованием defaultdict

```python
from collections import defaultdict

data = defaultdict(lambda: "N/A", {'name': 'Charlie'})
formatted_string = "Name: {name}, Age: {age}".format_map(data)
print(formatted_string)  # Вывод: Name: Charlie, Age: N/A
```
В этом примере мы используем defaultdict, чтобы вернуть значение "N/A" для отсутствующего ключа age.

▎Пример 4: Использование пользовательских объектов

Метод format_map() также может работать с пользовательскими объектами, если они реализуют метод __getitem__.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getitem__(self, key):
        return getattr(self, key)

person = Person("Diana", 28)
formatted_string = "Name: {name}, Age: {age}".format_map(person)
print(formatted_string)  # Вывод: Name: Diana, Age: 28
```

Здесь мы создали класс Person и реализовали метод __getitem__, чтобы позволить доступ к атрибутам объекта через плейсхолдеры.

▎Пример 5: Смешивание с обычными строками

Вы также можете использовать метод format_map() вместе с обычными строками.

```python
name = "Eve"
age = 22
formatted_string = "Name: {name}, Age: {age}".format_map({'name': name, 'age': age})
print(formatted_string)  # Вывод: Name: Eve, Age: 22
```

Здесь мы передаем значения в виде словаря прямо в метод format_map().

### Шаблоны строк с использованием модуля string

    В Python модуль string предоставляет несколько полезных инструментов для работы со строками, включая шаблоны строк. Основной класс, который мы будем использовать для создания шаблонов, — это Template. Этот класс позволяет удобно заменять плейсхолдеры в строках на соответствующие значения.

▎Основы работы с шаблонами строк

▎Импортирование модуля

Для начала необходимо импортировать класс Template из модуля string:
```python
from string import Template
```
▎Создание шаблона

Вы можете создать шаблон, используя специальный синтаксис с символом $ для обозначения плейсхолдеров. Например:

```python
template = Template("Hello, $name! You are $age years old.")
```

▎Замена плейсхолдеров

Для замены плейсхолдеров в шаблоне используется метод substitute(). Он принимает аргументы в виде словаря или именованных аргументов.

▎Пример 1: Использование словаря

```python
from string import Template

template = Template("Hello, $name! You are $age years old.")
data = {'name': 'Alice', 'age': 30}
result = template.substitute(data)
print(result)  # Вывод: Hello, Alice! You are 30 years old.
```

В этом примере мы создали шаблон и заменили плейсхолдеры значениями из словаря data.

▎Пример 2: Использование именованных аргументов

Вы также можете передавать значения напрямую:

```python
from string import Template

template = Template("Hello, $name! You are $age years old.")
result = template.substitute(name='Bob', age=25)
print(result)  # Вывод: Hello, Bob! You are 25 years old.
```
▎Обработка отсутствующих ключей

Если вы попытаетесь заменить плейсхолдер, для которого нет соответствующего значения, метод substitute() вызовет исключение KeyError. Чтобы избежать этого, можно использовать метод safe_substitute(), который просто пропустит отсутствующие ключи.

▎Пример 3: Использование safe_substitute()

```python
from string import Template

template = Template("Hello, $name! You are $age years old.")
data = {'name': 'Charlie'}
result = template.safe_substitute(data)
print(result)  # Вывод: Hello, Charlie! You are $age years old.
```

Здесь вместо ошибки мы получаем строку с отсутствующим значением для age.

▎Шаблоны с более сложными структурами

Шаблоны могут быть использованы для более сложных строк, включая форматы с несколькими плейсхолдерами.

▎Пример 4: Сложные шаблоны

```python
from string import Template

template = Template("$greeting, $name! Today is $day.")
data = {
    'greeting': 'Good morning',
    'name': 'Diana',
    'day': 'Monday'
}
result = template.substitute(data)
print(result)  # Вывод: Good morning, Diana! Today is Monday.
```

▎Использование шаблонов в классах

Вы можете также использовать шаблоны внутри классов для динамического создания строк.

▎Пример 5: Класс с шаблоном

```python
from string import Template

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduction(self):
        template = Template("Hi, I'm $name and I'm $age years old.")
        return template.substitute(name=self.name, age=self.age)

person = Person("Eve", 22)
print(person.introduction())  # Вывод: Hi, I'm Eve and I'm 22 years old.
```