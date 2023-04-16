#include <iostream>
#include <vector>
using namespace std;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int result = 0, n = 0, m = 0;
vector<vector<int>> board, checked, scoreBoard;

int main() {
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		vector<int> temp;
		for (int j = 0; j < m; j++) {
			int temp2;
			cin >> temp2;
			temp.push_back(temp2);
		}
		board.push_back(temp);
	}

	checked = vector<vector<int>>(n, vector<int>(m, false));
	scoreBoard = vector<vector<int>>(n, vector<int>(m, 0));

	for (int y = 0; y < n; y++) {
		for (int x = 0; x < m; x++) {
			if (checked[y][x] == false && board[y][x] != 1) {
				vector<vector<int>> curStack = {{y, x, y, x}}; //node : starty, startx, currenty, currentx, currentScore
				
				while (!curStack.empty()) {
					auto curElem=curStack.back();
					curStack.pop_back();
					checked[curElem[2]][curElem[3]] = true;
					
					if (board[curElem[2]][curElem[3]] == 0) 
						scoreBoard[curElem[0]][curElem[1]] += 1;
					else 
						scoreBoard[curElem[0]][curElem[1]] -= 2;
					
					for (int i = 0; i < 4; i++) {
						int nx = curElem[3] + dx[i], ny  = curElem[2] + dy[i];
						if (nx > -1 && nx < m && ny > -1 && ny < n && board[ny][nx] != 1 && checked[ny][nx] == false) {
							checked[ny][nx] = true;
							curStack.push_back({curElem[0], curElem[1], ny, nx});
						}
					}
				}
				int cur = scoreBoard[y][x]; 

				if (cur > result) {
					result = cur;
				}
			}
		}
	}

	cout << result << endl;
}