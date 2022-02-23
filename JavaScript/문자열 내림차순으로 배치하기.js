function solution(s) {
  let arr = s.split("");

  arr.sort(function (a, b) {
    if (a < b) return 1;
    if (a > b) return -1;
    if (a === b) return 0;
  });

  return arr.join("");
}
