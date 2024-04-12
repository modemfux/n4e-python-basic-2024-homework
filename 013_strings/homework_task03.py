# Task3: Работа с байтовой последовательностью

# Task3.1: Преобразование в utf-8
# С оборудования получили следующий вывод,
# нужно преобразовать его в unicode (utf-8) строку.

output = (
    b"\r\nHuawei Versatile Routing Platform Software"
    b"\r\nVRP (R) software, Version 8.220 (CE6857EI V200R022C00SPC500)"
    b"\r\nCopyright (C) 2012-2022 Huawei Technologies Co., Ltd."
    b"\r\nHUAWEI CE6857-48S6CQ-EI uptime is 248 days, 3 hours, 14 minutes\r\n"
)

print("Task 3.1")
print(output)
print(f"output type = {type(output)}")

output_utf = output.decode(encoding="utf-8")
print(output_utf)
print(f"output_utf type = {type(output_utf)}", end="\n" * 2)

# Task3.2: Возврат каретки (CR)
# У полученной в Task3.1 строки избавится от символа возврата каретки.

print("Task 3.2")
print(f'CR in output: {"\r" in output_utf}')
output_utf = output_utf.replace("\r", "")
print(r"Replace \r to ''")
print(f'CR in output: {"\r" in output_utf}', end="\n" * 2)

# Task3.3: Пробельные символы
# У полученной в Task3.2 строки удалить пробельные символы
# только с начала строки.
print("Task 3.3")
print(f'Space symbols at start: {output_utf.startswith("\n")}')
print(f'Space symbols at end: {output_utf.endswith("\n")}')
output_utf = output_utf.lstrip()
print("Use lstrip method on output_utf")
print(f'Space symbols at start: {output_utf.startswith("\n")}')
print(f'Space symbols at end: {output_utf.endswith("\n")}')
