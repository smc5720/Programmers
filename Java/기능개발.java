import java.util.ArrayList;
import java.util.Stack;

class Solution {
	public Integer[] solution(int[] progresses, int[] speeds) {
		ArrayList<Integer> answer = new ArrayList<Integer>();
		Stack<Integer> stack = new Stack<>();
		int cnt = 1;
		for (int i = 0; i < progresses.length; i++) {
			// tmp에는 작업이 완료되는 시간이 저장된다.
			int tmp = (100 - progresses[i]) / speeds[i]; 
			
			if (((100 - progresses[i]) % speeds[i]) > 0) {
				tmp += 1;
			}

			if (i == 0) {
				stack.push(tmp);
			} else {
				// 현재 시간이 최고 시간보다 많다면
				if (tmp > stack.peek()) {
					answer.add(cnt);
					cnt = 1;
					stack.push(tmp);
				} else {
					cnt += 1;
				}
			}
		}
		
		answer.add(cnt);
		
		return answer.toArray(new Integer[answer.size()]);
	}
}