function solution(fees, records) {
  const answer = [];
  // 차 번호 배열
  const carNumbers = [];
  // 입/출차 시간 기록
  const parkingLogs = {};
  const baseTime = fees[0];
  const baseFee = fees[1];
  const extraTime = fees[2];
  const extraFee = fees[3];

  for (let record of records) {
    let data = record.split(" ");
    let time = data[0];
    let carNum = data[1];

    if (!carNumbers.includes(carNum)) {
      carNumbers.push(carNum);
      parkingLogs[carNum] = [];
    }

    parkingLogs[carNum].push(time);
  }

  carNumbers.sort();

  for (let carNum of carNumbers) {
    if (parkingLogs[carNum].length % 2 == 1) {
      parkingLogs[carNum].push("23:59");
    }
  }

  for (let carNum of carNumbers) {
    answer.push(
      calculateFee(parkingLogs[carNum], baseTime, baseFee, extraTime, extraFee)
    );
  }

  return answer;
}

function calculateFee(parkingLog, baseTime, baseFee, extraTime, extraFee) {
  let totalTime = 0;
  let fee = 0;
  let inTime, outTime;

  for (let i = 0; i < parkingLog.length; i++) {
    // 입차 시간
    if (i % 2 == 0) {
      inTime = getMinutes(parkingLog[i]);
    }
    // 출차 시간
    else {
      outTime = getMinutes(parkingLog[i]);
      totalTime += outTime - inTime;
    }
  }

  totalTime -= baseTime;
  fee += baseFee;

  if (totalTime > 0) {
    fee += Math.ceil(totalTime / extraTime) * extraFee;
  }

  return fee;
}

function getMinutes(time) {
  let t = time.split(":");
  let hour = parseInt(t[0]);
  let min = parseInt(t[1]);

  return hour * 60 + min;
}
