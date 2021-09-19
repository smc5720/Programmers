import java.util.ArrayList;
import java.util.Stack;

class Solution {
	public Integer[] solution(int[] progresses, int[] speeds) {
		ArrayList<Integer> answer = new ArrayList<Integer>();
		Stack<Integer> stack = new Stack<>();
		int cnt = 1;
		for (int i = 0; i < progresses.length; i++) {
			// tmp���� �۾��� �Ϸ�Ǵ� �ð��� ����ȴ�.
			int tmp = (100 - progresses[i]) / speeds[i]; 
			
			if (((100 - progresses[i]) % speeds[i]) > 0) {
				tmp += 1;
			}

			if (i == 0) {
				stack.push(tmp);
			} else {
				// ���� �ð��� �ְ� �ð����� ���ٸ�
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