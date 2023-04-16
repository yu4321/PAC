board,checked,scoreBoard =[],[],[]

dx= [1,-1,0,0,-1,-1,1,1] # 8 directions
dy= [0,0,1,-1,-1,1,-1,1]

spX,spY,epX,epY=0,0,0,0

h, w = list(map(int,input().split()))
board=[[0 for j in range(w)] for i in range(h)]
scoreBoard=[[0 for j in range(w)] for i in range(h)]
checked=[[False for j in range(w)] for i in range(h)]

for y in range(h):
	curInput=input()
	for x in range(w):
		if curInput[x]=='E':
			board[y][x]=-9
			epX,epY = x,y
		elif curInput[x]=='S':
			board[y][x]=9
			spX,spY = x,y
		elif curInput[x]=='P':
			board[y][x]=-1
			for t in range(8):
				ny=y+dy[t]
				nx=x+dx[t]
				if (ny>=h) or (ny<0) or (nx>=w) or (nx<0):
					continue
				scoreBoard[ny][nx]+=1
curStack=[[spY,spX]]
curScore=0
while(curStack):
	cy,cx = curStack.pop()
	checked[cy][cx]=True
	if(board[cy][cx] == -1):
		curScore+=(scoreBoard[cy][cx]-3)
	elif(board[cy][cx] == 0):
		curScore+=scoreBoard[cy][cx]
	elif(board[cy][cx]==-9):
		break
	
	candits=[]
	for t in range(4):
		ny=cy+dy[t]
		nx=cx+dx[t]
		if (ny>=h) or (ny<0) or (nx>=w) or (nx<0) or (checked[ny][nx]):
			continue
		
		cv=board[ny][nx]
		
		if(cv==-9):
			candits=[[ny,nx]]
			break
		
		if(len(candits)==0):
			candits=[[ny,nx]]
			continue
			
		curCandit=board[candits[0][0]][candits[0][1]]
		
		if(cv<curCandit):
			candits=[[ny,nx]]
			continue
			
		candits.append([ny,nx])
	candits.sort(key=lambda x : (x[0], x[1]))
	curStack.append(candits[0])
		
print(curScore)
