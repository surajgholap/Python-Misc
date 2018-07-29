# Function that finds the peak
def peak(arr):
    if len(arr) != 0:
        lenNum = len(arr)
    else:
        print('Empty list cannot be processed')
        # raise Exception('Empty list cannot be processed')
    if int(lenNum/2) != 0 and arr[int(lenNum/2)] < arr[int(lenNum/2) - 1]:
        peak(arr[:int(lenNum/2)])
    elif int(lenNum/2) != lenNum - 1 and arr[int(lenNum/2)] < arr[int(lenNum/2
                                                                      ) + 1]:
        peak(arr[int(lenNum/2):])
    else:
        print(arr[int(lenNum/2)])


# Array passed to the function
nums = []
peak(nums)
