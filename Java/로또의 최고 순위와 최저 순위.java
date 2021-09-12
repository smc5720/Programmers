import java.util.Arrays;

public class Solution {
	public boolean func(int n, int[] arr) {
		for (int i = 0; i < arr.length; i++) {
			if (n == arr[i]) {
				return true;
			}
		}

		return false;
	}

	public int[] solution(int[] lottos, int[] win_nums) {
		int[] answer = { 0, 0 };
		int correct_num = 0;
		int zero_num = 0;

		for (int i = 0; i < lottos.length; i++) {
			if (lottos[i] == 0) {
				zero_num += 1;
				continue;
			}

			if (func(lottos[i], win_nums)) {
				correct_num += 1;
			}
		}

		answer[0] = 7 - (correct_num + zero_num);
		answer[1] = 7 - correct_num;
		
		if (answer[0] > 6) {
			answer[0] = 6;
		}
		
		if (answer[1] > 6) {
			answer[1] = 6;
		}

		return answer;
	}
}