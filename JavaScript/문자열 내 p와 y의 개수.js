function solution(s) {
  let p = 0;
  let y = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] == "p" || s[i] == "P") {
      p += 1;
    } else if (s[i] == "y" || s[i] == "Y") {
      y += 1;
    }
  }

  return p == y;
}