x,y,w,h = map(int,input().split())

route_distance = [x,y, w-x, h-y]
# 처음에 list() 이 안에 4개 넣어서 망했음
# list() 안에는 리터러블한거 하나만 들어가야함...!
print(min(route_distance))