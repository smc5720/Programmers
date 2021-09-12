function solution(array, commands) {
    var answer = [];

    for (var t in commands) {
        var i = commands[t][0];
        var j = commands[t][1];
        var k = commands[t][2];

        var tmp = array.slice(i - 1, j);

        tmp.sort(function (a, b){
            return a - b;
        });
        
        answer.push(tmp[k - 1]);
    }

    return answer;
}