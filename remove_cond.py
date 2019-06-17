sample = ['pass', 'fail', 'NA', 'pending', 'fail', 'pending', 'pending',
          'pending', 'pending', 'pending']


def rem_pend_fail(arr):
    "Function to remove pending and fail occuring in seq"
    i = 0
    j = 1
    # index = []
    while j != len(arr):
        if arr[j] == 'pending' and arr[i] == 'fail':
            index = i
            break
        i += 1
        j += 1
    # print(index)
    # for i in reversed(index):
    #     del arr[i]
    try:
        del arr[index:]
    except:
        print("No pending after fail")
    return arr


print(rem_pend_fail(sample))
