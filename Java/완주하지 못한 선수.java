package coding_test;

import java.util.HashMap;

public class Solution {
	public String solution(String[] participant, String[] completion) {
		HashMap<String, Integer> map = new HashMap<String, Integer>();

		for (int i = 0; i < participant.length; i++) {
			String key = participant[i];
			if (map.containsKey(key)) {
				Integer value = map.get(key);
				map.put(key, value + 1);
			} else {
				map.put(key, 1);
			}
		}

		for (int i = 0; i < completion.length; i++) {
			String key = completion[i];
			Integer value = map.get(key);
			map.put(key, value - 1);
		}

		for (int i = 0; i < participant.length; i++) {
			String key = participant[i];
			Integer value = map.get(key);
			if (value > 0) {
				return key;
			}
		}

		return "error";
	}
}