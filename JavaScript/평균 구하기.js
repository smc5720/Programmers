function solution(arr) {
  var answer = 0;

  for (let i of arr) {
    answer += i;
  }

  return answer / arr.length;
}
