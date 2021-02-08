#include <string>
#include <vector>
#include <math.h>
#include <iostream>

using namespace std;

// https://programmers.co.kr/learn/courses/30/lessons/17681

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
	vector<string> answer;

	for (int i = 0; i < n; i++)
	{
		int number1, number2;

		int num;
		num = n - 1;

		string str1, str2;
		str1 = "";
		str2 = "";

		number1 = arr1[i];
		number2 = arr2[i];

		while (num >= 0)
		{
			int p;
			p = pow(2, num);

			if (number1 / p == 1)
			{
				str1 += '1';
				number1 -= p;
			}

			else
			{
				str1 += '0';
			}

			if (number2 / p == 1)
			{
				str2 += '1';
				number2 -= p;
			}

			else
			{
				str2 += '0';
			}

			num -= 1;
		}

		string ans;
		ans = "";

		for (int j = 0; j < n; j++)
		{
			if (str1[j] == '0' && str2[j] == '0')
			{
				ans += " ";
			}

			else
			{
				ans += "#";
			}
		}

		answer.push_back(ans);
	}

	return answer;
}