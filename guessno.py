import random


rand_num = random.randint(0, 20)
print('Hello, What is your name?')
name = input()
print('Well, ' + name + ', Guess a number in my mind')


while True:
    num = input()
    num = int(num)
    if num > rand_num:
        print('Your guess is high')
    elif num < rand_num:
        print('Your guess is low')
    else:
        print('Right guess!')
        break