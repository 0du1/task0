## Завдання 2

Python скрипт, що маніпулює рядка, а саме:
1. Приймає рядок, та виділяє з нього всі чиса в окремий масив
2. Друкує рядок без чисел і масив чисел
3. Змінює регістр першої букви у всіх словах в рядку
4. Знаходить максимальне значення в масиві чисел
5. Решту чисел підносить до степеню по їх індексу
6. Результат записує в окремий масив

# Опис програми

На початку программа просить ввести ряд, з яким потрібно працювати.

Далі, программа перевіряє кожен символ в цьому рядку, і якщо він являється числом, программа заносить його в окремий ряд,якщо символ не являється число, то заносить в інший

![prog1](https://github.com/0du1/task0/blob/master/task1/img/prog1.png)

Друк масиву счисел та рядку без чисел


![prog2](https://github.com/0du1/task0/blob/master/task1/img/prog2.png)

Потім, йде робота з рядком. Програма робить першу і останню букву, в кожному слові рядка, великими.

![prog3](https://github.com/0du1/task0/blob/master/task1/img/prog3.png)


Далі программа шукає максимальне значення, серед чисел в "массиві"

![prog4](https://github.com/0du1/task0/blob/master/task1/img/prog4.png)

Всі числа, окрім найбільшого записуються в інший масив і підносятся до степені свого індексу.

![prog5](https://github.com/0du1/task0/blob/master/task1/img/prog5.png)

# Коміти

Клонуємо та перевіряємо на наявність локальних змін

![clone](https://github.com/0du1/task0/blob/master/task1/img/clone.png)
![status](https://github.com/0du1/task0/blob/master/task1/img/status.png)

Як бачимо, папка горить червоним.

Далі, ми використовуємо команду git add .

![add](https://github.com/0du1/task0/blob/master/task1/img/add.png)

Як бачимо, папка вже горить зеленим кольором, тобто вона готова до завантаження на GitHub

Зараз потрібно використати 2 команди, це `git commit -m "Add task1"`

![commit](https://github.com/0du1/task0/blob/master/task1/img/commit.png)

А також, `git push origin master` для завантаження змін

![push](https://github.com/0du1/task0/blob/master/task1/img/push.png)

Як можна спостерігати на скріншоті, зміни завантажились

![fin](https://github.com/0du1/task0/blob/master/task1/img/fin.png)

