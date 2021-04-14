#include <string>
#include <vector>
#include <map>
#include <math.h>

using namespace std;

int solution(string s) {
	int answer = s.length();
	int maxSize;
	maxSize = s.length() / 2;

	for (int i = 1; i <= maxSize; i++)
	{
		int idx;
		idx = 0;

		string t;
		vector <string> v;

		while (idx + i < s.length())
		{
			t = s.substr(idx, i);
			v.push_back(t);
			idx += i;
		}

		t = s.substr(idx, s.length() - idx);
		v.push_back(t);

		string c;
		int cnt, ans;
		ans = 0;

		for (int j = 0; j < v.size(); j++)
		{
			if (j == 0)
			{
				c = v[j];
				cnt = 1;
			}

			else
			{
				if (c == v[j])
				{
					cnt += 1;
				}

				else
				{
					ans += c.length();

					if (cnt > 1)
					{
						ans += log10(cnt) + 1;
					}

					c = v[j];
					cnt = 1;
				}
			}
		}

		ans += c.length();

		if (cnt > 1)
		{
			ans += log10(cnt) + 1;
		}

		answer = min(answer, ans);
	}

	return answer;
}