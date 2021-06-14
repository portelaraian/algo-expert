# O(nlog(n)) Time Complexity | O(1) Space Complexity
# Where n is the number of queries
def minimumWaitingTime(queries):
    queries.sort()
    # Amount of time that it must wait
    total_waiting_time = 0

    for i in range(len(queries)):
        if i == 0:
            pass
        else:
            total_waiting_time += sum(queries[:i])

    return total_waiting_time
