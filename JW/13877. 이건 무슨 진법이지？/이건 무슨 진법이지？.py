

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
        tf_list.append(int  (input_num))
    except ValueError:
        tf_list.append(0)

    #16진수로 해석
    for j in range(len(input_num)):
        output_num_16 += (16 ** (len(input_num)-1-j)) * int(input_num[j])
    tf_list.append(output_num_16)

    print(*tf_list) #리스트 풀어서 출력



            