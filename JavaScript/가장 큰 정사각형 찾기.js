function solution(board) {
  let max = 0;

  for (let y = 0; y < board.length; y++) {
    for (let x = 0; x < board[0].length; x++) {
      if (y == 0 || x == 0) {
        if (board[y][x] == 1) {
          if (max == 0) {
            max = 1;
          }
        }

        continue;
      }

      if (board[y][x] == 0) {
        continue;
      }

      if (max == 0) {
        max = 1;
      }

      let val = 10000000;

      if (y - 1 >= 0) {
        val = Math.min(val, board[y - 1][x] + 1);
      }

      if (x - 1 >= 0) {
        val = Math.min(val, board[y][x - 1] + 1);
      }

      if (y - 1 >= 0 && x - 1 >= 0) {
        val = Math.min(val, board[y - 1][x - 1] + 1);
      }

      if (val < 10000000) {
        max = Math.max(max, val);
        board[y][x] = val;
      }
    }
  }

  return max * max;
}
