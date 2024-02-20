# 문제
# C, C++, Java와 같은 프로그래밍 언어에서는 사용자가 다양한 진법의 상수를 사용할 수 있도록 "접두 문자(Prefix characters)"라는 개념을 도입하고 있다.

# 8진법인 수를 표기하고 싶으면, "0(숫자 0)"을, 16진법은 "0x"를, 10진법은 아무런 표기를 하지 않아도 되는데, 이해를 돕기 위해 10진법 수 "4660"을 이 표기방법대로 8, 10, 16진법으로 표기한 예는 다음과 같다.

# 8진법(Octal): 011064
# 10진법(Decimal): 4660
# 16진법(Hexadecimal): 0x1234
# 만약 이런 표기 방법이 없었다면, 컴파일러는 저 숫자가 8진법인지, 10진법인지, 16진법인지 알 길이 없다. 0x1234에서 "0x"라는 접두 문자가 빠지면 사용자가 16진수로 표기했지만, 컴파일러는 이를 16진수가 아닌 8진수, 10진수로 인식할 수도 있다는 소리다.

# 이러한 오류가 발생했을 경우를 가정하여, 10진법으로 표현 가능한 숫자들로 구성된 문자열을 각각 8진수, 10진수, 16진수로 해석하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에는 테스트 케이스를 나타내는 자연수 T(1 ≤ T ≤ 10000)이 주어진다. 이후 아래 2 ~ T + 1번째 줄에는 테스트 데이터의 번호를 나타내는 정수 K와 10진수로 표현된 문자열이 주어진다. 문자열의 길이는 7보다 작거나 같고, 0으로 시작할 수 있다.

# 출력
# 각각의 테스트 데이터마다 테스트 데이터의 번호 K와 8진법, 10진법, 16진법으로 나타낸 수를 공백으로 구분하여 출력한다. 만약 입력된 문자열이 8진수로 해석될 수 없는 경우에는 0을 출력한다.

# 입력 예제
# 4
# 1 1234
# 2 9
# 3 1777
# 4 129
# 출력 예제
# 1 668 1234 4660
# 2 0 9 9
# 3 1023 1777 6007
# 4 0 129 297



num_cases = int(input())
cases_data = []

for _ in range(num_cases):
    input_line = input()
    case_data = list(input_line.split())
    cases_data.append(case_data)



for i in range(num_cases):
    tf_list = []
    #시퀀스 숫자
    tf_list.append(cases_data[i][0])
    
    #초기화
    input_num = cases_data[i][1]
    output_num_8 = 0
    output_num_16 = 0

    #8진수로 해석
    if str(input_num).find("9") != -1 or str(input_num).find("8") != -1:
        output_num_8 = 0
    elif input_num[0] == "0":
        input_num = input_num[1:]
        for j in range(len(input_num)):
            output_num_8 += (8 ** (len(input_num)-1-j)) * int(input_num[j])
    else:
        for j in range(len(input_num)):
            output_num_8 += (8 ** (len(input_num)-1-j)) * int(input_num[j])
    tf_list.append(output_num_8)

    #10진수로 해석
    try:
        tf_list.append(int(input_num))
    except ValueError:
        tf_list.append(0)

    #16진수로 해석
    for j in range(len(input_num)):
        output_num_16 += (16 ** (len(input_num)-1-j)) * int(input_num[j])
    tf_list.append(output_num_16)

    print(*tf_list) #리스트 풀어서 출력



            