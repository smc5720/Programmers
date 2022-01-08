function solution(n) {
  if (n % 2 === 1) {
    return 2;
  }

  let answer = 0;
  let root = Math.sqrt(n - 1);

  for (let i = 2; i <= root; i++) {
    if ((n - 1) % i === 0) {
      return i;
    }
  }

  return n - 1;
}
