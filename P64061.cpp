#include <string>
#include <vector>
#include <stack>
using namespace std;

// https://programmers.co.kr/learn/courses/30/lessons/64061

int solution(vector<vector<int>> board, vector<int> moves)
{
	int answer = 0;
	stack <int> st[31];

	int row, col;
	row = board.size();
	col = board[0].size();

	for (int i = row - 1; i >= 0; i--)
	{
		for (int j = 0; j < col; j++)
		{
			if (board[i][j] != 0)
			{
				st[j + 1].push(board[i][j]);
			}
		}
	}

	int mvSize;
	mvSize = moves.size();

	for (int i = 0; i < mvSize; i++)
	{
		int pos;
		pos = moves[i];

		if (!st[pos].empty())
		{
			int top;
			top = st[pos].top();
			st[pos].pop();

			if (!st[0].empty() && st[0].top() == top)
			{
				st[0].pop();
				answer += 2;
			}

			else
			{
				st[0].push(top);
			}
		}
	}

	return answer;
}