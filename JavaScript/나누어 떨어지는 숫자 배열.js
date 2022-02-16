function solution(arr, divisor) {
  var answer = [];

  for (let a of arr) {
    if (a % divisor == 0) {
      answer.push(a);
    }
  }

  if (answer.length == 0) {
    answer.push(-1);
  }

  answer.sort(function (a, b) {
    return a - b;
  });

  return answer;
}
