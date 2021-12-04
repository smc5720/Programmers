function solution(s) {
  let answer = [];
  const numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];

  while (s.length > 0) {
    if (48 <= s.charCodeAt(0) && s.charCodeAt(0) <= 57) {
      answer.push(s.charAt(0));
      s = s.substring(1);
      continue;
    }

    for (let i = 0; i < numbers.length; i++) {
      if (s.startsWith(numbers[i])) {
        answer.push(String(i));
        s = s.substring(numbers[i].length);
        continue;
      }
    }
  }

  return Number(answer.join(""));
}
