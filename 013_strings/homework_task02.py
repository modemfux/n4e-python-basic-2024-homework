# Task2: Преобразовании числа в строку

# Перевести число в строку минимум 3 способами
#
# bd_id = 555
#
# bd_id_str1 = <ваше решение тут>
# bd_id_str2 = <ваше решение тут>
# bd_id_str3 = <ваше решение тут>

bd_id = 555

bd_id_str1 = str(bd_id)
print(f"bd_id_str1 is 'str': {isinstance(bd_id_str1, str)}")
print(f"bd_id_str1 = {bd_id_str1}", end="\n" * 2)

bd_id_str2 = f"{bd_id}"
print(f"bd_id_str2 is 'str': {isinstance(bd_id_str2, str)}")
print(f"bd_id_str2 = {bd_id_str2}", end="\n" * 2)

bd_id_str3 = "{}".format(bd_id)
print(f"bd_id_str3 is 'str': {isinstance(bd_id_str3, str)}")
print(f"bd_id_str3 = {bd_id_str3}")
