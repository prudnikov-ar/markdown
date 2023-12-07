"""
Вариант 9
"""

# Завершённая работа

def bold(s: str) -> str:
    pair = s.count("**")
    for _ in range(pair//2):
        s = s.replace("**", "<strong>", 1).replace("**", "</strong>", 1)
    return s


def itallic(s: str) -> str:
    once = s.count("*")
    for _ in range(once//2):
        s = s.replace("*", "<em>", 1).replace("*", "</em>", 1)
    return s


while True:

    print("Меню")
    print()
    print("Введите 1 если хотите отформатировать строку курсивом")
    print("Введите 2 если хотите отформатировать строку полужирным") 
    print("Введите 0 если хотите завершить программу")
    print()

    ans = input()
    if ans == "1":
        print("Введите строку")
        s = input()
        print("Ваша строка в отформатированнм виде:")
        print()
        print(itallic(s))
        print()
    elif ans == "2":
        print("Введите строку")
        s = input()
        print("Ваша строка в отформатированнм виде:")
        print()
        print(bold(s))
        print()
    elif ans == "0":
        print("Программа завершена")
        break
    else:
        print("Такой программы не существует")
        print()