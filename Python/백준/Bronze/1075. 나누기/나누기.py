N = input()
F = input()

q, r = divmod(int(N), int(F))

F_q = int(F)*q

if len(str(F_q)) < len(N):
    result = str(F_q + int(F))
    print(result[-2:])

else:
    string_num_00 = N[:-2] + '0' + '0'
    for i in range(100):
        result = int(string_num_00) + i
        if result % int(F) == 0:
            """실수한 부분
    #         print(str(result)[-2:])
    # string_num = str(F_q)
    # print('string_num:', string_num)


    # string_num_00 = string_num[:-2] + '0' + '0'
    # print('string_num_00:', string_num_00)
    
    # for i in range(100):
    #     result = int(string_num_00) + i
    #     print('result:', result)
    
    #     if result % int(F) == 0:"""
            print(str(result)[-2:])
            break