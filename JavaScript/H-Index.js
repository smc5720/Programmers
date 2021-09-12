function solution(citations) {
    citations.sort((a, b) => {
        return a - b;
    });

    let len = citations.length;
    // h-index가 될 값이다.
    let h = 0;

    for (var i = 0; i < len; i++) {
        while (citations[i] >= h && len - i >= h) {
            h += 1;
        }
    }

    return h - 1;
}