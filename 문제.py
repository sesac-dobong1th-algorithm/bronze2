# %%
from collections import Counter
while True:
    input_line = input().split()
    if input_line[0] == '#':  # 입력의 마지막
        break
    char = input_line[0]  # 찾을 소문자
    sentence = ' '.join(input_line[1:])  # 공백으로 구분된 문장 합치기
    word_count = Counter(sentence.lower())  # 문장을 소문자로 변환 후 카운트해서 각 문자별 개수 저장
    print(char, word_count[char])  # 해당 알파벳이 나타난 횟수 출력

# %%
