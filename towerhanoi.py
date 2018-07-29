import sys

# Function that recursively solves tower of hanoi
def tower(n, fr, to, sp):  # f - from , t - to, s - spare
    if n == 1:
        print('move from ' + str(fr) + ' to ' + str(to))
    else:
        tower(n-1, fr, sp, to)
        tower(1, fr, to, sp)
        tower(n-1, sp, to, fr)


# TODO: Call tower function with
# by passing the number of discs as an argument
num = int(sys.argv[1])
tower(num, 'f', 't', 's')