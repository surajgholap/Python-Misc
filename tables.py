def print_tables(base, times):
    for i in range(1, base+1):
        for j in range(1, times+1):
            print(i*j, end=" ")
        print()


print_tables(12, 12)
