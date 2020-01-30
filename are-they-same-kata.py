def comp(a,b):
    return sorted(a) == sorted([each * each for each in sorted(b)])