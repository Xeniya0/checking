import random

number = random.randint(0, 100)
print(number)
value = 0
while value != number:
    value = int(input('Угадай число: '))

    if value == number:
        print('маладес :D')
        break
    else:
        if value < number:
            print('выше бери')
        else:
            if value > number:
                print('бери меньше')

# a = int(input('теперь угадываю я, загадй число от 1 до 100: '))
# minn = 0
# maxi = 101
# num = 0
# while num != a:
#     if (minn < a) and (a < maxi):
#         num = random.randint(minn, maxi)
#         print("Твоё число: ", num, "?")
#         s = input("+/-/= : ")
#         if s == '+':
#             minn = num
#             num = random.randint(minn, maxi)
#             print("Твоё число: ", a, "?")
#             s = input("+/-/= : ")
#         elif s == '-':
#             maxi = num
#             num = random.randint(minn, maxi)
#             print("Твоё число: ", a, "?")
#             s = input("+/-/= : ")
#         else:
#             print("Yeeesss!!")
#             break
#     elif a == num:
#         print("Yeeesss!!")
#         break
#     else:
#         print("загадай число от 1 до 100")
#         break
