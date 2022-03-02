function isPrime(n) {
  if (n == 1) {
    return false;
  }

  if (n == 2) {
    return true;
  }

  let max = parseInt(Math.sqrt(n));

  for (let i = 2; i <= max; i++) {
    if (n % i == 0) {
      return false;
    }
  }

  return true;
}

function solution(n) {
  var answer = 0;

  for (let i = 1; i <= n; i++) {
    if (isPrime(i)) {
      answer += 1;
    }
  }

  return answer;
}
