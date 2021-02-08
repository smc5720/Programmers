#include <string>
#include <vector>

using namespace std;

// https://programmers.co.kr/learn/courses/30/lessons/67256

string solution(vector<int> numbers, string hand)
{
	string answer = "";
	int size;
	size = numbers.size();

	pair <int, int> keyPos[12];

	keyPos[1] = make_pair(0, 0); keyPos[2] = make_pair(0, 1); keyPos[3] = make_pair(0, 2);
	keyPos[4] = make_pair(1, 0); keyPos[5] = make_pair(1, 1); keyPos[6] = make_pair(1, 2);
	keyPos[7] = make_pair(2, 0); keyPos[8] = make_pair(2, 1); keyPos[9] = make_pair(2, 2);
	keyPos[10] = make_pair(3, 0); keyPos[0] = make_pair(3, 1); keyPos[11] = make_pair(3, 2);

	pair <int, int> leftPos;
	pair <int, int> rightPos;

	leftPos = keyPos[10];
	rightPos = keyPos[11];

	for (int i = 0; i < size; i++)
	{
		int numpad;
		numpad = numbers[i];

		if (numpad == 1 || numpad == 4 || numpad == 7)
		{
			answer += 'L';
			leftPos = keyPos[numpad];
		}

		else if (numpad == 3 || numpad == 6 || numpad == 9)
		{
			answer += 'R';
			rightPos = keyPos[numpad];
		}

		else
		{
			int leftVal, rightVal;

			leftVal = abs(leftPos.first - keyPos[numpad].first) + abs(leftPos.second - keyPos[numpad].second);
			rightVal = abs(rightPos.first - keyPos[numpad].first) + abs(rightPos.second - keyPos[numpad].second);

			if (leftVal > rightVal)
			{
				answer += 'R';
				rightPos = keyPos[numpad];
			}

			else if (leftVal < rightVal)
			{
				answer += 'L';
				leftPos = keyPos[numpad];
			}

			else
			{
				if (hand == "left")
				{
					answer += 'L';
					leftPos = keyPos[numpad];
				}

				else if (hand == "right")
				{
					answer += 'R';
					rightPos = keyPos[numpad];
				}
			}
		}
	}

	return answer;
}