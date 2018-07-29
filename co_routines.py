"""
Generators: produce values
Co_routine: 1)consume values, may not return anything, not for iteration, it
is built from a generator but it is conceptually different
2)Repeatedly receives input, Processes input and stops at yield statement
3)Each time you call the function, you are calling the same function, on the
other hand, has properties and states that can be referenced and altered.
Maintaining and using the state is what a coroutine object does. Persistent
properties can be changed and altered.
"""


def coroutine_example():
    while True:
        x = yield
        # do something with x
        print(x)


def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print(item)
                else:
                    print('No match')
            else:
                print('Not a string')
    except GeneratorExit:
        print(count)


if __name__ == '__main__':
    c = coroutine_example()
    c.__next__()
    c.send(10)
    c.close()
    d = counter('California')
    d.__next__()
    d.send('Ca')
    d.close()
