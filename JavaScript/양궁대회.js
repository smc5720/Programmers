function solution(n, info) {
  return simulate(n, info);
}

function simulate(n, info) {
  let maxVal = 0;
  let resArr = [[-1]];

  for (let i = 0; i < 2048; i++) {
    let arr = binary(i);

    if (sum(arr) <= n) {
      if (compareArray(arr, info) <= n) {
        let winScore = getWinScore(arr, info);

        if (maxVal > winScore) {
          continue;
        }

        if (winScore > 0) {
          const res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

          for (let i = 0; i <= 10; i++) {
            if (arr[i] === 1) {
              res[i] = info[i] + 1;
            }
          }

          if (sum(res) < n) {
            res[10] += n - sum(res);
          }

          if (maxVal === winScore) {
            resArr.push(res);
          } else if (maxVal < winScore) {
            resArr = [res];
            maxVal = winScore;
          }
        }
      }
    }
  }

  if (resArr[0][0] === -1) {
    return [-1];
  }

  return getMaxArr(resArr);
}

function getMaxArr(resArr) {
  let maxVal = 0;
  let result = [];

  for (let arr of resArr) {
    let num = calABS(arr);
    if (num > maxVal) {
      maxVal = num;
      result = arr;
    }
  }

  return result;
}

function calABS(arr) {
  let num = "";

  for (let i = arr.length - 1; i >= 0; i--) {
    num += arr[i];
  }

  return parseInt(num);
}

// arr의 조합을 완성하기 위해 필요한 화살의 개수를 반환한다.
function compareArray(arr, info) {
  let totalArrow = 0;

  for (let i = 0; i <= 10; i++) {
    if (arr[i] === 1) {
      totalArrow += info[i] + 1;
    }
  }

  return totalArrow;
}

// 현재 arr의 조합이 info 조합을 몇 점차로 이기는지 반환한다.
function getWinScore(arr, info) {
  let arrScore = 0;
  let infoScore = 0;

  for (let i = 0; i <= 10; i++) {
    let score = 10 - i;
    if (arr[i] === 1) {
      arrScore += score;
    } else if (info[i] > 0) {
      infoScore += score;
    }
  }

  return arrScore - infoScore;
}

function binary(num) {
  const arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  let n = num;

  for (let i = Math.floor(Math.log2(num)); i >= 0; i--) {
    let x = Math.floor(n / Math.pow(2, i));
    arr[10 - i] = x;
    n -= Math.pow(2, i) * x;
  }

  return arr;
}

function sum(arr) {
  let total = 0;

  for (let n of arr) {
    total += n;
  }

  return total;
}
