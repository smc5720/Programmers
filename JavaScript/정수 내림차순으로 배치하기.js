function solution(n) {
  var answer = 0;
  const arr = [];

  while (n > 0) {
    let v = n % 10;
    n = Math.floor(n / 10);
    arr.push(v);
  }

  arr.sort(function (a, b) {
    return b - a;
  });

  for (let num of arr) {
    answer += num;
    answer *= 10;
  }

  return answer / 10;
}
