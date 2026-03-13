import random


a="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlina = int(input('Введите длину пароля:' ))
password = ''

for i in range(dlina):
    random_element = random.choice(a)
    password+=random_element

print(password)