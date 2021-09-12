import java.util.LinkedList;
import java.util.Queue;

class Solution {
	public int solution(int bridge_length, int weight, int[] truck_weights) {
		// ��� Ʈ���� �������µ� �ɸ��� �ּ� �ð��� �����Ѵ�.
		int answer = 0;
		Queue<Integer> queue = new LinkedList<>();

		for (int i = 0; i < bridge_length; i++) {
			queue.add(0);
		}

		// ���� �ٸ� �� ���Ը� �����Ѵ�.
		int now_weight = 0;
		// �ö� ������ Ʈ���� �ε����� �����Ѵ�.
		int truck_idx = 0;

		while (now_weight > 0 || truck_idx < truck_weights.length) {
			now_weight -= queue.poll();

			// System.out.print(answer + "��: ");

			// ��� ���� Ʈ���� ��� �ٸ� ���� �ö� ���
			if (truck_idx == truck_weights.length) {
				// System.out.println("��� Ʈ���� ���� �ö󰬴�.");
				queue.add(0);
				answer += 1;
				continue;
			}

			// ���� �ٸ� ���� Ʈ���� ���� �ö� �� �ִ��� �Ǵ��Ѵ�.
			if (weight - now_weight >= truck_weights[truck_idx]) {
				// �ö� �� �ִٸ�
				// System.out.println(truck_idx + "��° Ʈ�� " + truck_weights[truck_idx] + "¥�� ���� �ö󰬴�.");
				now_weight += truck_weights[truck_idx];
				queue.add(truck_weights[truck_idx]);
				truck_idx += 1;
			} else {
				// �ö� �� ���ٸ�
				// System.out.println("�� �ö󰣴�.");
				queue.add(0);
			}
	
			answer += 1;
		}

		return answer;
	}
}