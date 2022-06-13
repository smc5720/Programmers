class Solution {
	int move = 0;

	public int[][] solution(int n) {
		int cnt = (int) Math.pow(2, n) - 1;
		int[][] answer = new int[cnt][2];

		hanoi(n, 1, 2, 3, answer);

		return answer;
	}

	public void hanoi(int n, int start, int mid, int dest, int[][] answer) {
		if (n == 0) {
			return;
		}

		// n번 원반을 dest로 옮기기 위해서는 먼저 위의 원반 n-1개들을 mid로 옮겨야 한다.
		hanoi(n - 1, start, dest, mid, answer);

		// n번 원반을 dest로 옮긴다.
		answer[move][0] = start;
		answer[move++][1] = dest;

		// mid에 있던 원반 n-1개들을 dest로 옮겨야 한다.
		hanoi(n - 1, mid, start, dest, answer);
	}
}