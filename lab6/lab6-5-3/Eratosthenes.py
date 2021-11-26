def eratosthenes(n):
    answer = []
    number = [True] * n
    for i in range(2, n):
        if i ** 2 <= n:
            if number[i]:
                for j in range(i**2, n, i):
                    if j <= n:
                        number[j] = False
    for i in range(len(number)):
        if number[i]:
            answer.append(str(i))
    return ' '.join(answer)
