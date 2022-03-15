function solution(n) {
  let val = Math.sqrt(n);

  if (n % val == 0) {
    return (val + 1) ** 2;
  }

  return -1;
}
