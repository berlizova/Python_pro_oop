def geometric_progression(first_elem, ratio):
    current = first_elem
    while True:
        yield current
        current *= ratio


# initial data
first_elem = 2
common_ratio = 5
gen = geometric_progression(first_elem, common_ratio)


for _ in range(8):
    print(next(gen))
