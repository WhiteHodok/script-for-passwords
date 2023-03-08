import random

''' 
Это простенький скрипт,который поможет мне в дальнейшем для реализации проги с регой в нужных сервисах.
Он может пригодиться людям,кто опасается стилаков без детекта,крадущих инфу из буфера обмена.
Всё будет реализовано с помощью самых простых алгоритмов и библиотек.
'''

# Здесь можно задать необходимые символы,на которые не будет ругаться сервис.00
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = int(input('Количество паролей?'+ "\n"))
length = int(input('Длина пароля?'+ "\n"))

for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)



