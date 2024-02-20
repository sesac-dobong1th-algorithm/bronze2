N = int(input())
a = {}
for num_decimal in range(2, N+1):
    sum = 0
    q= N            # 이거 하나 못해서 한시간 날림. N값 보존을위해서 변수가 3개 필요했음. N, q, quantity...
    while q:
        quantity, r = divmod(q, num_decimal)
        sum += r
        q = quantity
        
    a[num_decimal]= sum # 문법 실수 했었음. 그냥 num_decimal 하면 되는데, {num_deciaml} 이랬음. ;;


sum_list = list(a.values())
b = max(sum_list)

key_list = list(a.keys())
# key_list 만들어서 뒤에 if 문 이용해서 일치하는 가장 작은 key값 뽑는 것이 best안임.
# 괜히 sum값으로 key 만들었다가 sum 바뀔때 마다 해당 sum에 따른 진법도 갱신되어 버리니까
# 지금 이 문제는 동일한 sum 값이면 최소가 나와야하는데 전혀 나오지가 않았음.
# 2시간 걸려서 풀었음... 이게 맞나 싶네..



num = []
for key in key_list:
    if a[key] == b:
        num.append(key)
        

    

print(int(b), min(num))