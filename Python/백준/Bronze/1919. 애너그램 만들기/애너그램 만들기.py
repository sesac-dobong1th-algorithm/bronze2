str1 = input()
str2 = input()

re_str1 = list(str1)
re_str2 = list(str2)

for alpha in str1:
    if alpha in re_str2:
        re_str1.remove(alpha)
        re_str2.remove(alpha)


result = len(re_str1) + len(re_str2)
print(result)