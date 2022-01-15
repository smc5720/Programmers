function solution(id_list, report, k) {
  const answer = [];
  // (key, value) : (신고 당한 사람, 신고한 사람)
  const report_list = {};
  const mail_count = {};

  for (let id of id_list) {
    report_list[id] = [];
    mail_count[id] = 0;
  }

  for (let rep of report) {
    let tmp = rep.split(" ");

    if (!report_list[tmp[1]].includes(tmp[0])) {
      report_list[tmp[1]].push(tmp[0]);
    }
  }

  for (let id of id_list) {
    if (report_list[id].length >= k) {
      for (let reporter of report_list[id]) {
        mail_count[reporter] += 1;
      }
    }
  }

  for (let id of id_list) {
    answer.push(mail_count[id]);
  }

  return answer;
}
