#include <string>
#include <vector>
#include <math.h>
#include <iostream>
#include <map>

using namespace std;

// https://programmers.co.kr/learn/courses/30/lessons/17682

int solution(string dartResult) {
	int answer = 0;
	int length;
	length = dartResult.length();

	int sum;
	sum = 0;

	int pNum;
	pNum = 0;

	for (int i = 0; i < length; i++) {
		char c;
		c = dartResult[i];

		if (c >= '0' && c <= '9') {
			if (c == '1' && dartResult[i + 1] == '0') {
				i += 1;
				sum = 10;
			}
			else {
				sum = c - '0';
			}
		}

		else if (c == 'S') {
			sum = pow(sum, 1);
			if (i + 1 < length && dartResult[i + 1] == '#') {
				sum = (-1) * sum;
				i += 1;
			}
			else if (i + 1 < length && dartResult[i + 1] == '*') {
				sum *= 2;
				answer += pNum;
				i += 1;
			}
			answer += sum;
			pNum = sum;
		}

		else if (c == 'D') {
			sum = pow(sum, 2);
			if (i + 1 < length && dartResult[i + 1] == '#') {
				sum = (-1) * sum;
				i += 1;
			}
			else if (i + 1 < length && dartResult[i + 1] == '*') {
				sum *= 2;
				answer += pNum;
				i += 1;
			}
			answer += sum;
			pNum = sum;
		}

		else if (c == 'T') {
			sum = pow(sum, 3);
			if (i + 1 < length && dartResult[i + 1] == '#') {
				sum = (-1) * sum;
				i += 1;
			}
			else if (i + 1 < length && dartResult[i + 1] == '*') {
				sum *= 2;
				answer += pNum;
				i += 1;
			}
			answer += sum;
			pNum = sum;
		}
	}

	return answer;
}