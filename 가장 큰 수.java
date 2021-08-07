import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Numb {
	// 원래 숫자를 저장한다.
	Integer origin;
	// 바뀐 숫자를 저장한다.
	Integer change;
	// 원래 숫자의 길이를 저장한다.
	int origin_len;

	public Numb(Integer origin) {
		this.origin = origin;

		String tmp = origin.toString();
		this.origin_len = tmp.length();

		int idx = 0;

		while (tmp.length() < 4) {
			tmp += tmp.charAt(idx % origin_len);
			idx += 1;
		}

		change = Integer.parseInt(tmp);
	}

	public void display() {
		System.out.println("\n원래 숫자: " + origin);
		System.out.println("바뀐 숫자: " + change);
	}

	public String getNum() {
		return origin.toString();
	}
}

class Solution {
	public String solution(int[] numbers) {
		String answer = "";
		ArrayList<Numb> arr = new ArrayList<Numb>();

		for (int i = 0; i < numbers.length; i++) {
			Numb tmp = new Numb(numbers[i]);
			arr.add(tmp);
		}

		// 오름차순 정렬
		Collections.sort(arr, new Comparator<Numb>() {
			@Override
			public int compare(Numb n1, Numb n2) {
				return n1.change.compareTo(n2.change);
			}
		});

		// 내림차순으로 변경
		Collections.reverse(arr);

		for (int i = 0; i < arr.size(); i++) {
			String tmp = arr.get(i).getNum();
			
			if (answer.equals("") && tmp.equals("0") && i + 1 < arr.size()) {
				continue;
			}
			
			answer += arr.get(i).getNum();
		}

		return answer;
	}
}