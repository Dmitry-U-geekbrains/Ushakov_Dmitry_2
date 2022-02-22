# 3. Есть два списка:
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
from sys import getsizeof

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def my_gen():
    len_klasses = len(klasses)
    return ((tut, klasses[i]) if i < len_klasses else (tut, None) for i, tut in enumerate(tutors))


if __name__ == '__main__':
    gen = my_gen()
    print(*gen)
