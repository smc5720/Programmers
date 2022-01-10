function solution(s) {
  let len = s.length;

  if (len % 2 == 0) {
    return s.substr(len / 2 - 1, 2);
  }

  return s.substr(Math.floor(len / 2), 1);
}
