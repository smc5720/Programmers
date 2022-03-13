function solution(n) {
  var answer = [];

  while (n > 0) {
    answer.push(parseInt(n % 10));
    n = parseInt(n / 10);
  }

  return answer;
}
