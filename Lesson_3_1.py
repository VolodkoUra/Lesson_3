"""Присваивание"""
spam = 'Spam'
print(spam, sep="\n")
spam, ham = "yum", "YUM"
print(spam, ham, sep="\t")
[spam, ham] = ['yumi', "YUMI"]
print(spam, ham)
a, b, c, d = 'spam'
print(a, b, c, d, sep="\t")
a, *b = 'spam'
print(a,b, sep="\t")


"""
Задание 3.03
Ввести предложение состоящее из двух слов. 
Поменять местами слова, добавить восклицательный знак 
в начало и конец, вывести итоговое предложение на экран.
"""
string_all = input("Введите предложение из 2-ух слов: ")
string_result = string_all.split(" ")
print(string_result)
string_result2 = " ".join(string_result)
string_result3 = "!" + string_result2 +"!"

print(string_result3)


exit()
"""
Запросить у пользователя два целых числа.
Вывести строку вида “2 плюс 3 равно 5”Примечание: 
после ввода переменных преобразовать переменные к типу int
"""
x = int(input("Введите число x: "))
y = int(input("Введите число y: "))

result = x + y
print("{} плюс {} равно {}".format(x, y, result))


"""Доп. функуии при работе со строками"""
my_string = 'Hello,_my_name_is_Alex'
string_list = my_string.split("_")
print(string_list)
print("-".join(string_list))


exit()
"""Форматирование строк"""
first_name = input("Введите ваше имя: ")
last_name = input("Введте вашу фамилию: ")

string_a = 'Hello, %s %s' % (first_name, last_name)
print(string_a)
string_b = "Hello, {} {}".format(first_name, last_name)
print(string_b)
string_c = f"Hello, {first_name} {last_name}"


