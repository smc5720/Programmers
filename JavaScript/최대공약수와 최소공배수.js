function solution(n, m) {
  let gt = gcd(n, m);
  let lt = (n * m) / gt;

  var answer = [gt, lt];

  return answer;
}

function gcd(a, b) {
  if (a < b) {
    let tmp = a;
    a = b;
    b = tmp;
  }

  let n = a % b;

  if (n == 0) {
    return b;
  }

  return gcd(b, n);
}
