"""
ТЕСТОВОЕ ЗАДАНИЕ
-----------------------------------------------------------------------------------------------------
За многие годы работы над проектом накопился значительный объем документации.
Иногда разработчику необходимо распечатать определенные страницы.
Он выписывает их номера в произвольном порядке через запятую.
Ваша задача – привести номера страниц для печати в нормализованный вид.

Входные данные:
В единственнной строке входных данных содержится список с номерами страниц, перечисленных через запятую.
В нём не меньше одного и не больше 100 чисел. Каждое число является натуральным и не превосходящим 1000. Номера страниц
могут повторяться. Кроме чисел и запятых никаких других символов во входных данных нет.

Выходные данные:
Вам необходимо вывести единственную строку с номерами страниц в формате l1-r1, l2-r2,...lk-rk, где ri + 1 < li+1 для
всех i от 1 до k-1, и li <= ri для всех. В этой страке должны быть все номера страниц из вводных данных без повторений.
В случае, если для некоторых i окажется, что li = ri, то этот номер следует записывать как li, а не li-li.
"""

num_str = "1,3,1,4,5,8,10,9,4,5,2,15,20,16,17,18,19,25"

def make_intervals(num_str):  #создаём функцию, где перебираем каждое число и проверяем общее количество вводных чисел
    str_list = num_str.split(",")
    int_list = []
    for st in str_list:
        int_list.append(int(st))
    if len(int_list) > 100:
        return "ERROR: count > 100"

    int_list.sort()

    res_l = []
    for i in int_list:
        if i > 1000:
            return "ERROR: num > 1000"
        elif i < 1:
            return "ERROR: num < 1"
        if i not in res_l:
            res_l.append(i)

    res_str = []   # начинаем собирать строку на вывод
    k = 0
    current_str_n = 0

    while k < len(res_l):
        if k == 0:
            res_str += str(res_l[current_str_n])
            res_str.append(",")
            current_str_n = 1
        else:
            if res_l[k] - res_l[k-1] == 1:

                if len(res_str) >= 3:
                    if res_str[current_str_n-2] == "-":
                        res_str[current_str_n - 1] = str(res_l[k])

                    else:
                        res_str.append("-")
                        res_str.append(str(res_l[k]))
                        current_str_n += 3
                        res_str.append(",")
                else:
                    res_str.append("-")
                    res_str.append(str(res_l[k]))
                    current_str_n += 3
                    res_str.append(",")

            else:
                res_str.append(str(res_l[k]))
                current_str_n += 2
                res_str.append(",")

        k += 1

    result = ""
    for ch in res_str:
        result += ch
    while result.find(",,") != -1:
        result = result.replace(",,", ",")
    while result.find(",-") != -1:
        result = result.replace(",-", "-")
    result = result.replace(",", ", ")
    return result[:-2]

print(make_intervals(num_str))