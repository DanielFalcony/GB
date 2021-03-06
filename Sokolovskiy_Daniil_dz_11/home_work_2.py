# 2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

print('Решение задачи №2')


class OwnError(Exception):
    def __init__(self, val):
        self.val = val


inp_data = input('Введите 1-е число: ')
inp_data_2 = input('Введите 2-е число: ')


try:
    inp_data = int(inp_data)
    inp_data_2 = int(inp_data_2)
    if inp_data_2 == 0:
        raise OwnError("Попытка деления на 0")
    else:
        print(f'{inp_data} / {inp_data_2} = {inp_data / inp_data_2}')
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
