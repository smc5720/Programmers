function solution(numbers) {
    var answer = '';
    let arr = [];
    let max_length = 4;

    for (var i in numbers) {
        max_length = Math.max(max_length, String(numbers[i]).length);
    }

    for (var i in numbers) {
        let tmp = String(numbers[i]);
        let len = tmp.length;
        let n = max_length - len;

        for (var j = 0; j < n; j++) {
            tmp += tmp[j % len];
        }

        arr.push([tmp, i]);
    }

    arr.sort((a, b) => {
        return parseInt(b[0]) - parseInt(a[0]);
    })

    for (var i in arr) {
        answer += String(numbers[arr[i][1]]);
    }

    while (answer[0] === "0" && answer.length > 1) {
        answer = answer.substring(1);
    }

    return answer;
}