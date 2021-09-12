function solution(genres, plays) {
    var answer = [];
    let dict = {};
    let genres_dict = {};

    for (var i in genres) {
        if (genres[i] in dict) {
            dict[genres[i]] += plays[i];
            genres_dict[genres[i]].push([plays[i], parseInt(i)]);
        } else {
            dict[genres[i]] = plays[i];
            genres_dict[genres[i]] = [[plays[i], parseInt(i)]];
        }
    }

    let arr = [];

    for (var i in dict) {
        arr.push([dict[i], i]);
        genres_dict[i].sort(function (a, b) {
            var tmp = b[0] - a[0];
            if (tmp == 0) {
                return a[1] - b[1];
            } else {
                return tmp;
            }
        });
    }

    arr.sort(function (a, b) {
        return b[0] - a[0];
    });

    for (var i in arr) {
        var now_genre = arr[i][1];
        for (var j = 0; j < Math.min(2, genres_dict[now_genre].length); j++) {
            answer.push(genres_dict[now_genre][j][1]);
        }
    }

    return answer;
}