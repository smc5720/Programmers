function solution(price, money, count) {
  let m = money;

  for (let i = 1; i <= count; i++) {
    m -= price * i;
  }

  if (m < 0) {
    return -1 * m;
  }

  return 0;
}
