function solution(n, k) {
  let answer = 0;
  let t_num = translate(n, k);
  const arr = [];

  for (let pn of t_num.split("0")) {
    if (pn !== "" && pn !== "1") {
      arr.push(parseInt(pn));
    }
  }

  for (let num of arr) {
    if (isPrime(num)) {
      answer += 1;
    }
  }

  return answer;
}

function translate(n, k) {
  let num = n;
  let x = logN(n, k);
  let result = "";

  for (let i = x; i >= 0; i--) {
    let p = Math.floor(num / Math.pow(k, i));
    result += p;
    num -= Math.pow(k, i) * p;
  }

  return result;
}

// 숫자 x의 log n 값을 반환
function logN(x, n) {
  return Math.floor(Math.log(x) / Math.log(n));
}

function isPrime(n) {
  let sq = Math.floor(Math.sqrt(n));
  for (let i = 2; i <= sq; i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}