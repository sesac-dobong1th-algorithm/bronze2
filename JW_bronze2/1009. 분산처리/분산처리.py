num_cases = int(input())
cases_data = []

for _ in range(num_cases):
    input_line = input()
    case_data = list(map(int, input_line.split()))
    cases_data.append(case_data)



for i in range(num_cases):
    a = cases_data[i][0]
    b = cases_data[i][1]
    c = []
    d = a
    while True:
        if d%10 !=0 and d%10 not in c:
            c.append(d%10)
            d = d*a
        elif d%10 == 0:
            break
        else:
            break

    if d%10 == 0:
        print(10)
    else:
        print(c[b%len(c)-1])