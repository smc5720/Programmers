import java.util.ArrayList;
import java.util.Arrays;

class Solution {
	public int solution(int n, int[] lost, int[] reserve) {
		int answer = n - lost.length;
		boolean[] arr = new boolean[n + 2];		
		ArrayList<Integer> lost_arr = new ArrayList<Integer>();

		Arrays.sort(lost);
		
		for (int i = 0; i <= n + 1; i++) {
			arr[i] = false;
		}
 
		for (int i = 0; i < reserve.length; i++) {
			arr[reserve[i]] = true;
		}

		for (int i = 0; i < lost.length; i++) {
			if (arr[lost[i]]) {
				answer += 1;
				arr[lost[i]] = false;
			} else {
				lost_arr.add(lost[i]);
			}
		}

		for (int i = 0; i < lost_arr.size(); i++) {
			int idx = lost_arr.get(i);
			if (arr[idx] == false) {
				if (arr[idx - 1]) {
					answer += 1;
					arr[idx - 1] = false;
				} else if (arr[idx + 1]) {
					answer += 1;
					arr[idx + 1] = false;
				}
			}
		}

		return answer;
	}
}