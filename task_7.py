# В секретном агентстве Super-Secret-no решили использовать «метод бутерброда» 
# для шифрования переписки своих сотрудников. Сначала буквы слова нумеруются в таком порядке: 
# первая буква получает номер 1, последняя буква — номер 2, вторая — номер 3, 
# предпоследняя — номер 4, потом третья… и так для всех букв (см. рисунок). 
# Затем все буквы записываются в шифр в порядке своих номеров.

# Например, слово sandwich зашифруется в shacnidw.
# Программист Super-Secret-no написал программу шифрования и уволился.
# Теперь агенты не могут понять, что они написали друг другу.

# Напишите программу-дешифратор, которая расшифровала бы введённые сообщения.
# Пример:
# Введите зашифрованное сообщение: shacnidw.
# Расшифрованное сообщение: sandwich.

text = input("Введите зашифрованное сообщение: ")

h = '' # Не определился как переменную обозвать,
t = '' # и тут тоже.
count = 0

for i in text:
    
    if count % 2 :
        t = i + t
    else:
        h += i
    
    count += 1
    
print(h + t)


# Подсмотрел только логику решения:
#     if i % 2: t = s[i] + t
#     else: h += s[i]



