function solution(num) {
  let answer = 0;
  let n = num;

  while (n != 1 && answer <= 500) {
    answer += 1;

    if (n % 2 == 0) {
      n /= 2;
    } else {
      n = n * 3 + 1;
    }
  }

  return answer > 500 ? -1 : answer;
} 
