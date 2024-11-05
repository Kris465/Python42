# Функции (методы) списков.

1. append(x): Добавляет элемент x в конец списка.

```python
   my_list = [1, 2, 3]
   my_list.append(4)
   print(my_list)  # Вывод: [1, 2, 3, 4]
```

2. extend(iterable): Расширяет список, добавляя элементы из итерируемого объекта.

```python
   my_list = [1, 2, 3]
   my_list.extend([4, 5])
   print(my_list)  # Вывод: [1, 2, 3, 4, 5]
```

3. insert(i, x): Вставляет элемент x на позицию i.

```python
   my_list = [1, 2, 3]
   my_list.insert(1, 'a')
   print(my_list)  # Вывод: [1, 'a', 2, 3]
```

4. remove(x): Удаляет первый элемент списка, равный x. Генерирует ошибку, если элемент не найден.

```python
   my_list = [1, 2, 3, 2]
   my_list.remove(2)
   print(my_list)  # Вывод: [1, 3, 2]
```

5. pop([i]): Удаляет элемент по индексу i и возвращает его. Если индекс не указан, удаляет и возвращает последний элемент.

```python
   my_list = [1, 2, 3]
   popped_element = my_list.pop()
   print(popped_element)  # Вывод: 3
   print(my_list)         # Вывод: [1, 2]
```

6. clear(): Удаляет все элементы из списка.

```python
   my_list = [1, 2, 3]
   my_list.clear()
   print(my_list)  # Вывод: []
```

7. index(x[, start[, end]]): Возвращает индекс первого элемента, равного x. Генерирует ошибку, если элемент не найден.

```python
   my_list = [1, 2, 3]
   my_list.clear()
   print(my_list)  # Вывод: []
```

8. count(x): Возвращает количество элементов в списке, равных x.

```python
   my_list = [1, 2, 3, 2]
   count_of_two = my_list.count(2)
   print(count_of_two)  # Вывод: 2
```

9. sort(key=None, reverse=False): Сортирует элементы списка на месте (по возрастанию по умолчанию).

```python
   my_list = [3, 1, 2]
   my_list.sort()
   print(my_list)  # Вывод: [1, 2, 3]
```

10. reverse(): Разворачивает элементы списка на месте.

```python
    my_list = [1, 2, 3]
    my_list.reverse()
    print(my_list)  # Вывод: [3, 2, 1]
```

11. copy(): Возвращает поверхностную копию списка.

```python
    my_list = [1, 2, 3]
    my_list.reverse()
    print(my_list)  # Вывод: [3, 2, 1]
```


