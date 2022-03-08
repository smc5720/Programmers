function solution(s, n) {
  var answer = "";

  for (let i = 0; i < s.length; i++) {
    if ("A" > s[i] || (s[i] > "Z" && s[i] < "a") || s[i] > "z") {
      answer += s[i];
      continue;
    }

    let max = "z";
    let min = "a";

    if (s[i] <= "Z") {
      max = "Z";
      min = "A";
    }

    let cn = s.charCodeAt(i) + n;

    if (cn > max.charCodeAt(0)) {
      cn = cn - max.charCodeAt(0) + min.charCodeAt(0) - 1;
    }

    answer += String.fromCharCode(cn);
  }

  return answer;
}
