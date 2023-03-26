# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n=int(input())
spduMap={}
foundSpeeds=[]
for cnt in range(n):
	speed, dur = list(int(x) for x in input().split())
	if(speed not in spduMap):
		spduMap[speed]=[dur,cnt+1]
		foundSpeeds.append(speed)
	else:
		if spduMap[speed][0]<=dur:
			spduMap[speed]=dur,cnt+1
ans=0
for s in foundSpeeds:
	ans+=spduMap[s][1]
print(ans)

