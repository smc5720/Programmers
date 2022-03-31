function solution(x) {
  return x % getNum(x) == 0;
}

function getNum(x) {
  let n = 0;

  while (x > 0) {
    n += x % 10;
    x = Math.floor(x / 10);
  }

  return n;
}