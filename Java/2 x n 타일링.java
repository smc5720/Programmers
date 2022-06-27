class Solution {
	public int solution(int n) {
		int[] dp = new int[n + 1];
		int div = 1000000007;

		dp[0] = 1;
		dp[1] = 1;

		for (int i = 2; i <= n; i++) {
			dp[i] = (dp[i - 1] % div) + (dp[i - 2] % div);
			dp[i] = dp[i] % div;
		}

		return dp[n];
	}
}