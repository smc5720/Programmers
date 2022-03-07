function solution(s) {
  let answer = 1;

  if (s[0] == "-") {
    s = s.substr(1, s.length - 1);
    answer = -1;
  }

  answer = answer * parseInt(s);

  return answer;
}
