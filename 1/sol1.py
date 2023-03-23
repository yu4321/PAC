n = int(input())
car_infos = []
car_dict = {}

for i in range(n):
	v,w = list(map(int, input().split()))
	if v in car_dict:
		if w >= car_dict[v][0]:
			car_dict[v] = [w,i+1]
	else:
		car_dict[v] = [w,i+1]
		
vals = car_dict.values()
result = 0
for val in vals:
	result += val[1]
print(result)
