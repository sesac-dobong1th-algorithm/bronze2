num_cases = int(input())
str_list = []

for _ in range(num_cases):
    input_str = input()
    str_list.append(input_str.lower())

#알파벳 모음 리스트
a2z = list("abcdefghijklmnopqrstuvwxyz")



def ispangram(input_str: str):

    #나타나지 않은 문자 저장 리스트
    missing_letters = []

    for i in a2z:
        if input_str.find(i) == -1:
            missing_letters.append(i)
    
    if len(missing_letters) ==0:
        print('pangram')
    else:
        print("missing", "".join(missing_letters))


for j in str_list:
    ispangram(j)