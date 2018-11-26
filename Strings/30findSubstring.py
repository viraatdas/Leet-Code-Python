import itertools

def findSubstring(s, words):
    permutations = []
    for i in range (2, len(words) + 1):
        temporary = list(itertools.permutations(words, i))
        permutations += temporary

    output = []

    for e in permutations:
        str = ''.join(e)
        try:
            output.append(s.index(str))
        except ValueError:
            pass

    print (output)
