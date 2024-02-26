import math
N = int(input())

for _ in range(N):
    message = input()
    length = len(message)
    X = math.sqrt(length)
    X = math.ceil(X)

    add_astro = int(X**2 - length)
    incode_message = list(message + ('*'*add_astro))

    result = [incode_message[i*X : X*(i+1)] for i in range(X)]
    submit = ""

    for index_2 in range(X):
        for index_1 in range(X):
            decode = result[X - index_1 - 1][index_2]
            if decode != '*':
                submit += decode
    print(submit)