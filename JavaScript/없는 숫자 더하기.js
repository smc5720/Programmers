function solution(numbers) {
  let answer = 45;

  for (let n of numbers) {
    answer -= n;
  }
  
  return answer;
}
