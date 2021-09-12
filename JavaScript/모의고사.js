function solution(answers) {
    var answer = [];

    let player = [[1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]];

    let arr = [];

    for (var j = 0; j < 3; j++) {
        var len = player[j].length;
        var cnt = 0;
        for (var i = 0; i < answers.length; i++) {
            var idx = i % len;
            if (player[j][idx] == answers[i]) {
                cnt += 1;
            }
        }
        arr.push(cnt);
    }

    let max_val = Math.max(...arr);

    for (var i = 0; i < 3; i++) {
        if (max_val == arr[i]) {
            answer.push(i + 1);
        }
    }

    return answer;
}