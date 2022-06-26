import java.io.*;
import java.util.*;

class Solution {
	public char[][] cGrid;
	public int[] dx = { -1, 0, 1, 0 };
	public int[] dy = { 0, -1, 0, 1 };
	public int[][][] visited;
	public int row, col;
	public ArrayList<Integer> path;
	public ArrayList<Pos> pos;

	public class Pos {
		int r, c, d;

		public Pos(int r, int c, int d) {
			this.r = r;
			this.c = c;
			this.d = d;
		}
	}

	public int[] solution(String[] grid) {
		int[] answer;

		row = grid.length;
		col = grid[0].length();

		visited = new int[row][col][4];
		cGrid = new char[row][col];

		path = new ArrayList<Integer>();

		for (int r = 0; r < row; r++) {
			for (int c = 0; c < col; c++) {
				cGrid[r][c] = grid[r].charAt(c);
			}
		}

		for (int r = 0; r < row; r++) {
			for (int c = 0; c < col; c++) {
				for (int d = 0; d < 4; d++) {
					pos = new ArrayList<Pos>();

					int v = 0;
					int tr = r;
					int tc = c;
					int td = d;

					while (visited[tr][tc][td] == 0) {
						visited[tr][tc][td] = v;
						pos.add(new Pos(tr, tc, td));

						if (cGrid[tr][tc] == 'L') {
							td -= 1;

							if (td < 0) {
								td = 3;
							}
						} else if (cGrid[tr][tc] == 'R') {
							td += 1;

							if (td > 3) {
								td = 0;
							}
						}

						tr = tr + dx[td];
						tc = tc + dy[td];

						if (tr < 0) {
							tr = row - 1;
						} else if (tr == row) {
							tr = 0;
						} else if (tc < 0) {
							tc = col - 1;
						} else if (tc == col) {
							tc = 0;
						}

						v += 1;
					}

					if (visited[tr][tc][td] == -1) {
						clear(0, 0);
					} else {
						path.add(v - visited[tr][tc][td]);
						clear(visited[tr][tc][td], v);
					}
				}
			}
		}

		Collections.sort(path);

		answer = new int[path.size()];

		for (int i = 0; i < path.size(); i++) {
			answer[i] = path.get(i);
		}

		return answer;
	}

	public void move(int r, int c, int d, int v) {

	}

	public void clear(int start, int finish) {
		for (Pos p : pos) {
			if (start <= visited[p.r][p.c][p.d] && visited[p.r][p.c][p.d] <= finish) {
				visited[p.r][p.c][p.d] = -1;
			} else {
				visited[p.r][p.c][p.d] = 0;
			}
		}
	}
}