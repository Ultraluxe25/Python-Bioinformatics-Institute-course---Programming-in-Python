'''
В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу,
по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".

Для того, чтобы это звучало правильно, для каждого 
n нужно использовать верное окончание слова.

Напишите программу, считывающую с пользовательского ввода целое число 
n (неотрицательное), выводящее это число в консоль вместе с правильным образом изменённым словом "программист",
для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.

В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.

Дополнительный комментарий к условию:
Обратите внимание, что задача не так проста, как кажется на первый взгляд. Если ваше решение не проходит какой-то тест, это значит,
то вы не рассмотрели какой-то из случаев входных данных (число программистов 
Обязательно проверяйте свои решения на дополнительных значениях, а не только на тех, что приведены в условии задания.

Так как задание повышенной сложности, вручную код решений проверяться не будет. Если вы столкнулись с ошибкой в первых четырёх тестах,
проверьте, что вы используете только русские символы для ответа. В остальных случаях ищите ошибку в логике работы программы.

Sample Input 1:
5
9
Sample Output 1:
5 программистов

Sample Input 2:
0

Sample Output 2:
0 программистов

Sample Input 3:
1

Sample Output 3:

1 программист

Sample Input 4:
2

Sample Output 4:
2 программиста
'''

a = int(input())
if a % 10 == 1 and a % 100 // 10 != 1:
    print(f'{a} программист')
elif (a % 10 == 2 or a % 10 == 3 or a % 10 == 4) \
and a % 100 // 10 != 1:
    print(f'{a} программиста')
else:
    print(f'{a} программистов')# put your python code here
    