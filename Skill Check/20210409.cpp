#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    int answer = 0;

    sort(A.begin(), A.end(), greater<int>());
    sort(B.begin(), B.end(), greater<int>());

    queue <int> qA, qB;

    int size;
    size = A.size();

    for (int i = 0; i < size; i++)
    {
        qA.push(A[i]);
        qB.push(B[i]);
    }

    while (!qA.empty())
    {
        if (qA.front() < qB.front())
        {
            answer += 1;
            qB.pop();
        }

        qA.pop();
    }

    return answer;
}