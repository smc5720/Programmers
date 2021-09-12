function solution(participant, completion) {
    var dict = {};

    for (var i in participant) {
        var person = participant[i]
        if (person in dict) {
            dict[person] += 1;
        } else {
            dict[person] = 1;
        }
    }

    for (var i in completion) {
        var person = completion[i]
        dict[person] -= 1;
    }

    for (var i in dict) {
        if (dict[i] == 1) {
            return i;
        }
    }

    return -1;
}