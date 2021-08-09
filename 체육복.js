function solution(n, lost, reserve) {
    var answer = n - lost.length;
    let arr = new Array(n + 2);
    let lost_arr = [];

    lost.sort((a, b) => { return a - b });

    for (var i = 0; i <= n + 1; i++) {
        arr[i] = false;
    }

    for (var i = 0; i < reserve.length; i++) {
        arr[reserve[i]] = true;
    }

    for (var i = 0; i < lost.length; i++) {
        // 여분의 체육복이 있는데 도난당한 경우
        if (arr[lost[i]]) {
            // lost 상태는 아니지만 남한테 빌려줄 수 없음
            answer += 1;
            arr[lost[i]] = false;
        } else {
            lost_arr.push(lost[i]);
        }
    }

    for (var i = 0; i < lost_arr.length; i++) {
        var idx = lost_arr[i];
        // 앞 사람이 체육복이 있는 경우
        if (arr[idx - 1]) {
            answer += 1;
            arr[idx - 1] = false;
        }
        // 뒷 사람이 체육복이 있는 경우
        else if (arr[idx + 1]) {
            answer += 1;
            arr[idx + 1] = false;
        }
    }

    return answer;
}