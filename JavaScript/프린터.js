function solution(priorities, location) {
    var answer = 0;
    let queue = []; 
    
    // 중요도를 따로 저장하고 현재 가장 높은 중요도가 얼마인지 확인한다.
    let rank = [];

    for (var i in priorities) {
        queue.push([priorities[i], parseInt(i)]);
        rank.push(priorities[i]);
    }

    // 중요도 배열을 내림차순으로 정렬한다.
    rank.sort(function (a, b) {
        return b - a;
    });

    while (queue.length != 0) {
        var tmp = queue.shift();
        if (rank[0] === tmp[0]) {
            answer += 1
            rank.shift();
            if (tmp[1] === location) {
                return answer;
            }
        } else {
            queue.push(tmp);
        }
    }

    return -1;
}