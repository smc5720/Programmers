function solution(s) {
  let answer = s.length;

  for (let i = 1; i < s.length; i++) {
    answer = Math.min(answer, zip(s, i).length);
  }

  return answer;
}

function zip(s, i) {
  let arr = [];
  let compWord = "";
  let count = 0;

  for (let j = 0; j < s.length; j += i) {
    let nowWord = s.substr(j, i);

    if (compWord === nowWord) {
      count += 1;
      continue;
    }

    if (count > 1) {
      arr.push(count);
    }

    arr.push(compWord);

    compWord = nowWord;
    count = 1;
  }

  if (count > 1) {
    arr.push(count);
  }

  arr.push(compWord);

  return arr.join("");
}
