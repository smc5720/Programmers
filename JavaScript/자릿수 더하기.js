function solution(n) {
  let answer = 0;

  while (n / 10 != 0 || n % 10 != 0) {
    let num = parseInt(n / 10);
    let other = n % 10;

    answer += other;
    n = num;
  }

  return answer;
}