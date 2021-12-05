function solution(s) {
  let answer = 0;
  const stack = [];
  let top = -1;

  if (stack.length % 2 !== 0) {
    return 0;
  }

  for (let i = 0; i < s.length; i++) {
    if (top === -1 || stack[top] !== s.charAt(i)) {
      stack.push(s.charAt(i));
      top += 1;
    } else {
      stack.pop();
      top -= 1;
    }
  }

  if (stack.length == 0) {
    answer = 1;
  }

  return answer;
}
