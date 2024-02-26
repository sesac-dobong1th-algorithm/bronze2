import sys



month_day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
years_29 = [1700,1800,1900,2100,2200]

while True:
    d, m, y  = map(int,sys.stdin.readline().split())
    if d+m+y == 0:
        break
    elif m == 1:
        days = d
    else:
        days = 0
        for i in range(m-1):
            days += month_day[i+1]
        if m>2 and (y%4==0) and (y not in years_29):
            days += 1
        days += d
    print(days)

