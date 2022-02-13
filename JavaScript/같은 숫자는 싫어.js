function solution(arr) {
  let answer = [];
  let n = -1;

  for (let i of arr) {
    if (n != i) {
      answer.push(i);
      n = i;
    }
  }

  return answer;
}
