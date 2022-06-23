import java.util.*;
import java.io.*;

class Solution {
	public char[] player = { 'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T' };
	public boolean[] visited = new boolean[8];
	public char[] tmp = new char[8];
	public HashMap<Character, Integer> hashMap = new HashMap<Character, Integer>();
	public int count = 0;

	public int solution(int n, String[] data) {
		for (int i = 0; i < 8; i++) {
			hashMap.put(player[i], -1);
		}

		combination(0, data);
		return count;
	}

	public void combination(int idx, String[] data) {
		if (idx == 8) {
			for (String d : data) {
				if (!check(d)) {
					return;
				}
			}

			count += 1;
			return;
		}

		for (int i = 0; i < 8; i++) {
			if (!visited[i]) {
				visited[i] = true;
				hashMap.put(player[i], idx);
				combination(idx + 1, data);
				visited[i] = false;
			}
		}
	}

	// a와 b 사이의 간격을 나타낸다.
	public int dist(char a, char b) {
		return Math.abs(hashMap.get(a) - hashMap.get(b)) - 1;
	}

	// 해당 조건이 올바른지 확인한다.
	public boolean check(String cond) {
		char a = cond.charAt(0);
		char b = cond.charAt(2);
		char op = cond.charAt(3);
		int dst = cond.charAt(4) - '0';

		if (op == '=') {
			// System.out.printf("%c(%d)는 %c(%d)와 %d만큼 떨어져있어야 한다. → %d\n", a,
			// hashMap.get(a), b, hashMap.get(b), dst, dist(a, b));
			return dist(a, b) == dst;
		} else if (op == '<') {
			// System.out.printf("%c(%d)는 %c(%d)와 %d보다 적게 떨어져있어야 한다. → %d\n", a,
			// hashMap.get(a), b, hashMap.get(b), dst, dist(a, b));
			return dist(a, b) < dst;
		} else {
			// System.out.printf("%c(%d)는 %c(%d)와 %d보다 많이 떨어져있어야 한다. → %d\n", a,
			// hashMap.get(a), b, hashMap.get(b), dst, dist(a, b));
			return dist(a, b) > dst;
		}
	}
}