function solution(s) {
  var answer = "";
  let gap = 32;
  let i = 0;

  for (let idx = 0; idx < s.length; idx++) {
    if (s[idx] == " ") {
      answer += " ";
      i = 0;
      continue;
    }

    if (i % 2 == 1) {
      if (s[idx] <= "Z") {
        answer += String.fromCharCode(s[idx].charCodeAt(0) + gap);
      } else {
        answer += s[idx];
      }
    } else {
      if (s[idx] >= "a") {
        answer += String.fromCharCode(s[idx].charCodeAt(0) - gap);
      } else {
        answer += s[idx];
      }
    }

    i += 1;
  }

  return answer;
}
