def get_counts_dict(s):
    counts = {}

    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    return counts
