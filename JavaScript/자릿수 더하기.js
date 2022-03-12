function logB(x, base) {
  return Math.log(x) / Math.log(base);
}

function solution(n) {
  let answer = 0;
  let size = parseInt(logB(n, 10));

  for (let i = 0; i <= size; i++) {
    let num = n % 10;
    n = parseInt(n / 10);
    answer += num;
  }

  return answer;
}
