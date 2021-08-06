import java.util.LinkedList;
import java.util.Queue;

class Solution {
	public int solution(int bridge_length, int weight, int[] truck_weights) {
		// 모든 트럭이 지나가는데 걸리는 최소 시간을 저장한다.
		int answer = 0;
		Queue<Integer> queue = new LinkedList<>();

		for (int i = 0; i < bridge_length; i++) {
			queue.add(0);
		}

		// 현재 다리 위 무게를 저장한다.
		int now_weight = 0;
		// 올라갈 차례인 트럭의 인덱스를 저장한다.
		int truck_idx = 0;

		while (now_weight > 0 || truck_idx < truck_weights.length) {
			now_weight -= queue.poll();

			// System.out.print(answer + "초: ");

			// 대기 중인 트럭이 모두 다리 위로 올라간 경우
			if (truck_idx == truck_weights.length) {
				// System.out.println("모든 트럭이 위로 올라갔다.");
				queue.add(0);
				answer += 1;
				continue;
			}

			// 현재 다리 위에 트럭이 새로 올라갈 수 있는지 판단한다.
			if (weight - now_weight >= truck_weights[truck_idx]) {
				// 올라갈 수 있다면
				// System.out.println(truck_idx + "번째 트럭 " + truck_weights[truck_idx] + "짜리 위로 올라갔다.");
				now_weight += truck_weights[truck_idx];
				queue.add(truck_weights[truck_idx]);
				truck_idx += 1;
			} else {
				// 올라갈 수 없다면
				// System.out.println("못 올라간다.");
				queue.add(0);
			}
	
			answer += 1;
		}

		return answer;
	}
}