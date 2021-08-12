import java.util.ArrayList;

class Button {
	public int y, x;

	public Button(int y, int x) {
		this.y = y;
		this.x = x;
	}

	public int func(int a, int b) {
		return Math.abs(a - y) + Math.abs(b - x);
	}
}

class Solution {
	public String solution(int[] numbers, String hand) {
		String answer = "";

		ArrayList<Button> arr = new ArrayList<Button>();

		arr.add(new Button(3, 1)); // 0

		arr.add(new Button(0, 0)); // 1
		arr.add(new Button(0, 1)); // 2
		arr.add(new Button(0, 2)); // 3

		arr.add(new Button(1, 0)); // 4
		arr.add(new Button(1, 1)); // 5
		arr.add(new Button(1, 2)); // 6

		arr.add(new Button(2, 0)); // 7
		arr.add(new Button(2, 1)); // 8
		arr.add(new Button(2, 2)); // 9

		arr.add(new Button(3, 0)); // *
		arr.add(new Button(3, 2)); // #

		int left = 10;
		int right = 11;

		for (int i = 0; i < numbers.length; i++) {
			int tmp = numbers[i];

			if (tmp == 1 || tmp == 4 || tmp == 7) {
				left = tmp;
				answer += "L";
				continue;
			} else if (tmp == 3 || tmp == 6 || tmp == 9) {
				right = tmp;
				answer += "R";
				continue;
			}

			int left_val = arr.get(tmp).func(arr.get(left).y, arr.get(left).x);
			int right_val = arr.get(tmp).func(arr.get(right).y, arr.get(right).x);

			if (left_val < right_val) {
				// System.out.println(left_val + " < " + right_val + " = 왼쪽");
				left = tmp;
				answer += "L";
			} else if (left_val > right_val) {
				// System.out.println(left_val + " > " + right_val + " = 오른쪽");
				right = tmp;
				answer += "R";
			} else {
				if (hand.equals("left")) {
					// System.out.println("왼손잡이니까 왼쪽");
					left = tmp;
					answer += "L";
				} else {
					// System.out.println("오른손잡이니까 오른쪽");
					right = tmp;
					answer += "R";
				}
			}
		}

		return answer;
	}
}