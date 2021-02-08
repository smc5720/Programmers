#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {
	string answer = new_id;
	int size;
	size = new_id.length();

	// 1단계: 대문자 → 소문자
	for (int i = 0; i < size; i++)
	{
		if (answer[i] >= 65 && answer[i] <= 90)
		{
			answer[i] = answer[i] + 32;
		}
	}

	new_id = answer;
	answer = "";
	size = new_id.length();

	// 2단계: 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
	for (int i = 0; i < size; i++)
	{
		if (new_id[i] >= 97 && new_id[i] <= 122)
		{
			answer += new_id[i];
		}

		else if (new_id[i] >= 48 && new_id[i] <= 57)
		{
			answer += new_id[i];
		}

		else if (new_id[i] == '-' || new_id[i] == '_' || new_id[i] == '.')
		{
			answer += new_id[i];
		}
	}

	new_id = answer;
	answer = "";
	size = new_id.length();

	// 3단계: 연속된 마침표 하나로 바꾸기
	for (int i = 0; i < size; i++)
	{
		if (i > 0)
		{
			if (new_id[i] == '.' && answer[answer.length() - 1] == new_id[i])
			{
				continue;
			}
		}

		answer += new_id[i];
	}

	new_id = answer;
	answer = "";
	size = new_id.length();

	// 4단계: 아이디의 처음이나 끝에 위치한 '.' 제거
	for (int i = 0; i < size; i++)
	{
		if (i == 0 || i == size - 1)
		{
			if (new_id[i] == '.')
			{
				continue;
			}
		}

		answer += new_id[i];
	}

	new_id = answer;
	size = new_id.length();

	// 5단계: 빈 문자열이라면, new_id에 "a"를 대입
	if (size == 0)
	{
		answer = "a";
	}

	new_id = answer;
	size = new_id.length();

	// 6단계: 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자 모두 제거
	// 제거 후 마침표(.)가 끝에 위치한다면 끝에 위치한 마침표(.) 문자 제거
	if (size >= 16)
	{
		answer = "";

		for (int i = 0; i < size; i++)
		{
			if (i < 14)
			{
				answer += new_id[i];
			}

			else if (i == 14)
			{
				if (new_id[i] != '.')
				{
					answer += new_id[i];
				}
			}
		}
	}

	new_id = answer;
	size = new_id.length();

	// 7단계: new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복
	if (size <= 2)
	{
		answer = new_id;

		while (answer.length() < 3)
		{
			answer += new_id[size - 1];
		}
	}

	return answer;
}