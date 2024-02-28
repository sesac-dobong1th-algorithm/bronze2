n = input()

i = 2
digit_sum_max = 0
knary = 105

while i <= int(n):    
    digit_sum = 0 
    k = int(n)
    for j in range(5, -1, -1):
        if k//(i**j) != 0:
            digit_sum += k//(i**j)
            k = k%(i**j)    
    if digit_sum > digit_sum_max:
        knary = i
        digit_sum_max = digit_sum
    elif digit_sum == digit_sum_max and i < knary:
        knary = i
    i += 1

print(digit_sum_max, knary)