function solution(arr) {
  let min = arr[0];
  let idx = 0;
  const answer = [];

  if (arr.length == 1) {
    return [-1];
  }

  for (let i = 1; i < arr.length; i++) {
    if (min > arr[i]) {
      min = arr[i];
      idx = i;
    }
  }

  for (let i = 0; i < arr.length; i++) {
    if (i == idx) {
      continue;
    }

    answer.push(arr[i]);
  }

  return answer;
}
