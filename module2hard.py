from random import randint


def trap(n):
    figure = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                figure += str(i) + str(j)
    return f'{n} - {figure}\nВам предначертано жить:)'


n = randint(3, 20)

n = int(input("Ну здравствуй, Индиана Джонс! Введи число и если оно будет кратно сумме каждой пары то останешся в живых: "))

indiana_jones = trap(n)
print(indiana_jones)