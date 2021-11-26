def dots(r):
    count = 0
    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            if x ** 2 + y ** 2 <= r ** 2:
                count += 1
    return count
