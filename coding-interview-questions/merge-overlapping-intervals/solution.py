def mergeOverlappingIntervals(intervals):
    intervals.sort()
    to_pop = []

    idx = 0
    while idx+1 <= len(intervals)-1:
        count = 1

        if intervals[idx][1] >= intervals[idx+count][0]:

            while intervals[idx][1] >= intervals[idx+count][0]:

                if intervals[idx][0] > intervals[idx+count][0]:
                    intervals[idx][0] = intervals[idx+count][0]
                if intervals[idx][1] < intervals[idx+count][1]:
                    intervals[idx][1] = intervals[idx+count][1]

                to_pop.append(idx+count)
                count += 1

                if (idx+count) > (len(intervals) - 1):
                    count -= 1
                    break

        if (intervals[idx][1] < intervals[idx+count][0]):
            idx = idx + count
        else:
            idx = idx + (count+1)

    for i in sorted(to_pop, reverse=True):
        intervals.pop(i)

    return intervals
