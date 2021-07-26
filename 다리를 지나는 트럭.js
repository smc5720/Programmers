function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let bridge = [];

    for (var i = 0; i < bridge_length; i++) {
        bridge.push(0);
    }

    let now_weight = 0;

    while (truck_weights.length > 0 || now_weight != 0) {
        answer += 1
        // 매 초마다 다리에서 나가는 트럭의 무게를 저장한다.
        var tmp_out = bridge.shift();
        now_weight -= tmp_out;

        if (now_weight + truck_weights[0] <= weight) {
            // 트럭이 하나 더 올라올 수 있다면
            bridge.push(truck_weights[0])
            now_weight += truck_weights.shift();
        } else {
            bridge.push(0)
        }
    }

    return answer;
}