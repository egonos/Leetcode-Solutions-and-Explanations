def rotLeft(a, d):
    rotations_actual = d%len(a)
    return a[rotations_actual:] + a[:rotations_actual]