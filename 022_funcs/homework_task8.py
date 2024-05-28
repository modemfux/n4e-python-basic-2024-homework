from datetime import datetime
from time import sleep

# ## Task8: Параметры по умолчанию
#
# Задача: написать функцию, которая печатает переданный ей текст добавляя
# временную метку (аналог логирования). Нужно иметь возможность явно указать
# временную метку, но если она не указана, то в качестве временной метки должно
# использовать время вызова функции. Под поставленную задачу написана функция
# `my_log`, принимающая текст сообщения (`msg`) и опционально временную метку
# (`dt`) со значенниме по умолчанию. Функция не работает как предполагается.
# Нужно исправить функцию.
#
# ```python
# from datetime import datetime
#
# def my_log(msg, *, dt=datetime.now()):
#     print(f"[{dt:%Y-%m-%d %H:%M:%S}]: {msg}")
#
# my_log("test")
# [2024-05-19 10:57:10]: test
#
# # ждем пару секунд ...
# my_log("test")
# [2024-05-19 10:57:10]: test
#
# # еще ждем ...
# my_log("test")
# [2024-05-19 10:57:10]: test
# ```
#

# Старое, некорректное решение
# def my_log(msg, *, dt=datetime.now):
#     print(f"[{dt():%Y-%m-%d %H:%M:%S}]: {msg}")


def my_log(msg: str, *, dt: str = "") -> None:
    if dt == "":
        dt = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    print(f"[{dt}]: {msg}")


if __name__ == "__main__":
    for i in range(3):
        my_log(f"Message {i}")
        sleep(2)
    my_log("Message!", dt="very strange dt!")
