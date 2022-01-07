function solution(sizes) {
  let maxX = 0;
  let maxY = 0;

  for (let i of sizes) {
    i.sort(function (a, b) {
      return a - b;
    });

    maxX = Math.max(i[0], maxX);
    maxY = Math.max(i[1], maxY);
  }

  return maxX * maxY;
}
