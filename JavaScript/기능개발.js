function solution(progresses, speeds) {
    var answer = [];
    let queue = [];

    for (var i in progresses) {
        queue.push(Math.ceil((100 - progresses[i]) / speeds[i]));
    }

    let now_var = 0;
    let tmp = 0;

    for (var i in queue) {
        if (now_var < queue[i]) {
            answer.push(tmp);
            tmp = 1;
            now_var = queue[i]
        } else {
            tmp += 1;
        }
    }

    answer.push(tmp);
    answer.shift();

    return answer;
}