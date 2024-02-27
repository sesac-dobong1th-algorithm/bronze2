dict = {}

while True:
    alpha = input()
    if alpha == '#':
        break
    else:
        list_alpha = alpha.split()
        dict[list_alpha[0]] = list_alpha[1:] 

for key, value in dict.items():
    sum_values = ('').join(value)
    sum_values = sum_values.lower()
    count_num = sum_values.count(key)
    print(f"{key}",f"{count_num}")
