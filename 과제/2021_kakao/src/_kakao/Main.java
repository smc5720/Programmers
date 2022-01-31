package _kakao;

import java.util.ArrayList;
import java.util.HashMap;

import org.json.JSONObject;
import org.json.JSONPointer;

public class Main {
	/*
	 * 0: 6초간 아무 것도 하지 않음 1: 위로 한 칸 이동 2: 오른쪽으로 한 칸 이동 3: 아래로 한 칸 이동 4: 왼쪽으로 한 칸 이동
	 * 5: 자전거 상차 6: 자전거 하차
	 */

	static final String NO_MOVE = "0";
	static final String UP = "1";
	static final String RIGHT = "2";
	static final String DOWN = "3";
	static final String LEFT = "4";
	static final String LOAD = "5";
	static final String SAVE = "6";

	static int centerR = 2;
	static int centerC = 2;

	public static HashMap<Integer, Pair> hashMap = new HashMap<>();

	static class Pair {
		int r, c;

		Pair(int a, int b) {
			r = a;
			c = b;
		}
	}

	private static JSONParser jsonParser = new JSONParser();

	public static void main(String[] args) {
		int problemId = 1;

		// Get Key
		String response = start(problemId);

		if (response.equals("200")) {
			int time = 0;
			makeMap(5, 5);

			while (time < 720) {
				time += 1;

				// 각 위치별로 부족한 것, 남는 것 체크
				ArrayList<Location> locations = getLocations();
				ArrayList<Truck> trucks = getTrucks();
				ArrayList<Command> commands = new ArrayList<>();
				ArrayList<Integer> order;
				ArrayList<Integer> order2;

				if (time % 50 == 1) {
					commands.add(new Command(0, getRoute(4, 0, hashMap.get(18).r, hashMap.get(18).c)));
					commands.add(new Command(1, getRoute(4, 0, hashMap.get(16).r, hashMap.get(16).c)));
					commands.add(new Command(2, getRoute(4, 0, hashMap.get(6).r, hashMap.get(6).c)));
					commands.add(new Command(3, getRoute(4, 0, hashMap.get(8).r, hashMap.get(8).c)));
					commands.add(new Command(4, getRoute(4, 0, hashMap.get(12).r, hashMap.get(12).c)));

					System.out.println(simulate(commands));
					continue;
				}

				int max = 4, maxIndex = 0, min = 4, minIndex = 0;
				int rest = locations.get(12).getLocated_bikes_count();

				for (Location l : locations) {
					int r = hashMap.get(l.getId()).r;
					int c = hashMap.get(l.getId()).c;

					int locationId = 0;

					if (l.getLocated_bikes_count() < 4) {
						// 3
						if (r <= 2 && c <= 2) {
							locationId = trucks.get(3).getLocation_id();
						}

						// 2
						if (r >= 2 && c <= 2) {
							locationId = trucks.get(2).getLocation_id();
						}

						// 0
						if (r <= 2 && c > 2) {
							locationId = trucks.get(0).getLocation_id();
						}

						// 1
						if (r > 2 && c > 2) {
							locationId = trucks.get(1).getLocation_id();
						}

						order = getRoute(hashMap.get(locationId).r, hashMap.get(locationId).c, centerR, centerC);

						int cnt = 4 - l.getLocated_bikes_count();
						int cur = l.getLocated_bikes_count();

						while (rest > 0 && order.size() < 10 && cnt != 0) {
							cnt -= 1;
							rest -= 1;
							order.add(5);
						}

						order.addAll(getRoute(centerR, centerC, hashMap.get(l.getId()).r, hashMap.get(l.getId()).c));

						while (order.size() < 10 && cur < 4) {
							cur += 1;
							order.add(6);
						}
					} else if (l.getLocated_bikes_count() > 4) {
						// 3
						if (r <= 2 && c <= 2) {
							locationId = trucks.get(3).getLocation_id();
						}

						// 2
						if (r >= 2 && c <= 2) {
							locationId = trucks.get(2).getLocation_id();
						}

						// 0
						if (r <= 2 && c > 2) {
							locationId = trucks.get(0).getLocation_id();
						}

						// 1
						if (r > 2 && c > 2) {
							locationId = trucks.get(1).getLocation_id();
						}

						order = getRoute(hashMap.get(locationId).r, hashMap.get(locationId).c, centerR, centerC);

						int cnt = 4 - l.getLocated_bikes_count();
						int cur = l.getLocated_bikes_count();

						while (rest > 0 && order.size() < 10 && cnt != 0) {
							cnt -= 1;
							rest -= 1;
							order.add(5);
						}

						order.addAll(getRoute(centerR, centerC, hashMap.get(l.getId()).r, hashMap.get(l.getId()).c));

						while (order.size() < 10 && cur < 4) {
							cur += 1;
							order.add(6);
						}
					}

					// 제일 많은 바이크가 있는 곳
					if (max < l.getLocated_bikes_count()) {
						max = l.getLocated_bikes_count();
						maxIndex = l.getId();
					}

					// 제일 적은 바이크가 있는 곳
					if (min > l.getLocated_bikes_count()) {
						min = l.getLocated_bikes_count();
						minIndex = l.getId();
					}
				}

				// 각 트럭이랑 거리 계산해서 제일 가까운 애가 싣는다.
				// 단, 아직 들어있는게 없다면 그 다음 애가 내린다.
				// 아무도 없으면 아무도 내리지 않는다.
			}
		}
	}

	private static int getDistance(int r, int c, int tr, int tc) {
		return Math.abs(tr - r) + Math.abs(tc - c);
	}

	private static ArrayList<Integer> getRoute(int r, int c, int tr, int tc) {
		ArrayList<Integer> orders = new ArrayList<>();

		if (r < tr) {
			for (int i = 0; i < tr - r; i++) {
				if (orders.size() < 10) {
					orders.add(3);
				}
			}
		} else {
			for (int i = 0; i < r - tr; i++) {
				if (orders.size() < 10) {
					orders.add(1);
				}
			}
		}

		if (c < tc) {
			for (int i = 0; i < tc - c; i++) {
				if (orders.size() < 10) {
					orders.add(2);
				}
			}
		} else {
			for (int i = 0; i < c - tc; i++) {
				if (orders.size() < 10) {
					orders.add(4);
				}
			}
		}

		return orders;
	}

	public static void makeMap(int R, int C) {
		int index = 0;

		for (int i = 0; i < C; i++) {
			for (int j = R - 1; j >= 0; j--) {
				hashMap.put(index++, new Pair(j, i));
			}
		}
	}

	private static ArrayList<Truck> getTrucks() {
		JSONObject jsonObject = Connection.getInstance().trucks();
		return jsonParser.getTruck(jsonObject);
	}

	private static ArrayList<Location> getLocations() {
		JSONObject jsonObject = Connection.getInstance().locations();
		return jsonParser.getLocations(jsonObject);
	}

	private static int getScore() {
		System.out.println("### API SCORE ###");
		JSONObject jsonObject = Connection.getInstance().score();

		return jsonParser.getScore(jsonObject);
	}

	private static String simulate(ArrayList<Command> commands) {
		JSONObject jsonObject = Connection.getInstance().simulate(jsonParser.getCommandsJSONArray(commands));
		Simulate simulate = jsonParser.putSimulation(jsonObject);

		return simulate.toString();
	}

	private static String start(int problemId) {
		System.out.println("### API START ###");
		String response = TokenManager.getInstance().createToken(problemId);
		System.out.println("Token : " + TokenManager.getInstance().getToken());
		return response;
	}
}
