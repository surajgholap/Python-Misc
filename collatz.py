# Write a function called collatz
def collatz(num):
    if num % 2 == 0:  # Check if the no is even or odd
        return num // 2  # If even, return num//2
    else:
        return 3 * num + 1    # If odd, r   return 3 * num +1


# Code to accept input from the user
print('Enter Number')
while(True):
    try:
        number = int(input())
    except:
        print('Enter numbers only')
        continue
    # TODO: Program to call function collatz until it returns 1
    check = collatz(number)
    print(check)
    if check != 1:
        continue
    else:
        break
