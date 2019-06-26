import memory_profiler
import random
import time

students = ['Lancer', 'Berserker', 'Archer', 'Saber', 'Caster', 'Rider']
grades = ['A', 'B', 'C', 'D', 'E']

print('Memory (Before): {}Mb'.format(memory_profiler.memory_usage()))


def grade_list(num):
    result = []
    for i in range(num):
        entry = {
            'id': i,
            'name': random.choice(students),
            'grade': random.choice(grades)
        }
        result.append(entry)
    return result


def grade_generator(num):
    for i in range(num):
        entry = {
            'id': i,
            'name': random.choice(students),
            'grade': random.choice(grades)
        }
        yield entry


# t1 = time.clock()
# people = grade_list(1000000)
# t2 = time.clock()
"""
Time taken for normal function
Memory (Before): [37.9921875]Mb
Memory (After): [309.7265625]Mb
Took 2.285797 Seconds
"""
t1 = time.clock()
people = grade_generator(1000000)
t2 = time.clock()
"""
Time taken for generator function
Memory (Before): [37.97265625]Mb
Memory (After): [37.97265625]Mb
Took 1.6000000000016e-05 Seconds
"""

print('Memory (After): {}Mb'.format(memory_profiler.memory_usage()))
print('Took {} Seconds'.format(t2-t1))
