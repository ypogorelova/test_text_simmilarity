def find_duplicate(ll):
    for ind, i in enumerate(sorted(ll)):
        if ind == 0:
            prev = i

        elif prev == i:
            return i

        else:
            prev = i

# if we sort an list, so duplicates will be pair of numbers next to each other.
# The time complexity of this solution is O(N log N)