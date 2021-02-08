#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {
	string answer = new_id;
	int size;
	size = new_id.length();

	// 1�ܰ�: �빮�� �� �ҹ���
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

	// 2�ܰ�: �ҹ���, ����, ����(-), ����(_), ��ħǥ(.)�� ������ ��� ���� ����
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

	// 3�ܰ�: ���ӵ� ��ħǥ �ϳ��� �ٲٱ�
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

	// 4�ܰ�: ���̵��� ó���̳� ���� ��ġ�� '.' ����
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

	// 5�ܰ�: �� ���ڿ��̶��, new_id�� "a"�� ����
	if (size == 0)
	{
		answer = "a";
	}

	new_id = answer;
	size = new_id.length();

	// 6�ܰ�: ���̰� 16�� �̻��̸�, ù 15���� ���ڸ� ������ ������ ���� ��� ����
	// ���� �� ��ħǥ(.)�� ���� ��ġ�Ѵٸ� ���� ��ġ�� ��ħǥ(.) ���� ����
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

	// 7�ܰ�: new_id�� ���̰� 2�� ���϶��, new_id�� ������ ���ڸ� new_id�� ���̰� 3�� �� ������ �ݺ�
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