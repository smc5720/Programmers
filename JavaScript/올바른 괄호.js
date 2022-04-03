function solution(s) {
  let cnt = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] == "(") {
      cnt += 1;
    } else {
      if (cnt == 0) {
        return false;
      }
      cnt -= 1;
    }
  }

  if (cnt == 0) {
    return true;
  } else {
    return false;
  }
}
