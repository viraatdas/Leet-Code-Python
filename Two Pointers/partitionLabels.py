def partitionLabels(self, S):
    lookup = {c: i for i, c in enumerate(S)}
    first = 0
    last = 0
    res = []

    for i, c in enumerate(S):
        last = max(last, lookup[c])
        if i == last:
            res.append(i - first + 1)
            first = i + 1

    return res
