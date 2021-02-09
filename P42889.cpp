#include <string>
#include <vector>
#include <math.h>
#include <iostream>
#include <map>

using namespace std;

// https://programmers.co.kr/learn/courses/30/lessons/42889

vector<int> solution(int N, vector<int> stages) {
	vector<int> answer;
	map<int, int> m;

	for (int i = 1; i <= N + 1; i++) {
		pair<int, int> p;
		p.first = i;
		p.second = 0;
		m.insert(p);
	}

	for (int i = 0; i < stages.size(); i++) {
		int nowStage;
		nowStage = stages[i];
		m[nowStage] += 1;
	}

	map<double, vector<int>> d;
	double num;
	num = stages.size();

	for (int i = 1; i <= N; i++) {
		double fail;
		fail = m[i] / num;
		num -= m[i];

		if (d.count(fail) > 0) {
			d[fail].push_back(i);
		}

		else {
			vector<int> v;
			v.push_back(i);
			d.insert(make_pair(fail, v));
		}
	}

	for (auto k = d.rbegin(); k != d.rend(); ++k) {
		int size;
		size = k->second.size();

		for (int i = 0; i < size; i++) {
			answer.push_back(k->second[i]);
		}
	}

	return answer;
}