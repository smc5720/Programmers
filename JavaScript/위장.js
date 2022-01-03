function solution(clothes) {
    let answer = 1;
    let dict = {};

    for (var i in clothes) {
        let tmp = clothes[i][1];
        if (tmp in dict) {
            dict[tmp] += 1;
        } else {
            dict[tmp] = 1;
        }
    }

    for (var i in dict) {
        answer *= dict[i] + 1
    }

    return answer - 1;
}