S = input()
K = input()

New_S = ""

for s in S:
    if s.isalpha():
        New_S += s

if K in New_S:
    print(1)
else:
    print(0)