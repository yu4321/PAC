# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

global result, n, m
result,n,m=0,0,0
global dx,dy
dx= [1,-1,0,0]
dy= [0,0,1,-1]
global board, checked, scoreBoard
board,checked, scoreBoard =[],[],[]


def checkBoard(y,x):
	global result, dx, dy, board, checked
	
	curVal=0
	checked[y][x]=True
	
	for i in range(4):
		nx, ny=x+dx[i],y+dy[i]
		if(nx>-1 and nx<m and ny>-1 and ny<n and board[ny][nx]!=1 and checked[ny][nx]==False):
			curVal+=checkBoard(ny,nx)
			
	if(board[y][x]==0):
		curVal+=1
	else:
		curVal-=2
		
	return curVal


n, m = list(map(int,input().split()))

for i in range(n):
	board.append(list(map(int,input().split())))

checked=[[False for j in range(m)] for i in range(n)]
scoreBoard=[[0 for j in range(m)] for i in range(n)]

for y in range(n):
	for x in range(m):
		if(checked[y][x]==False and board[y][x]!=1):
			curStack=[[y,x,y,x]] #node : starty, startx, currenty, currentx, currentScore
			
			while(curStack):
				sy,sx,cy,cx=curStack.pop()
				checked[cy][cx]=True
				if(board[cy][cx]==0):
					scoreBoard[sy][sx]+=1
				else:
					scoreBoard[sy][sx]-=2
					
				for i in range(4):
					nx, ny=cx+dx[i],cy+dy[i]
					if(nx>-1 and nx<m and ny>-1 and ny<n and board[ny][nx]!=1 and checked[ny][nx]==False):
						checked[ny][nx]=True
						curStack.append([sy,sx,ny,nx])
			
			#cur=checkBoard(y,x) - 재귀 사용시 여럿 Runtime Error
			cur=scoreBoard[y][x] # 현재 로직으로 하면 Runtime error는 없지만 여럿 Timeout
			if(cur>result):
				result=cur

print(result)