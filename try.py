def check_log_history(events):
    stack = []
    for idx, i in enumerate(events):
        lis = i.split(" ")
        if lis[0] == "ACQUIRE" and lis[1] not in stack:
            stack.append(lis[1])
        elif lis[0] == "ACQUIRE" and lis[1] in stack:
            return idx + 1
        elif(lis[0]) == "RELEASE" and lis[1] == stack[-1]:
            stack.pop()
        elif(lis[0]) == "RELEASE" and lis[1] != stack[-1]:
            return idx + 1
        else:
            return idx
    if len(stack) == 0:
        return 0
    else:
        return(len(events) + 1)


event = ["ACQUIRE 1", "ACQUIRE 2", "RELEASE 2", "RELEASE 1"]
event1 = ["ACQUIRE 83", "RELEASE 34", "RELEASE 2", "RELEASE 1"]
event2 = ["ACQUIRE 83", "ACQUIRE 34", "RELEASE 34"]
event3 = ["ACQUIRE 83", "ACQUIRE 34", "ACQUIRE 4"]

print(check_log_history(event))
print(check_log_history(event1))
print(check_log_history(event2))
print(check_log_history(event3))
