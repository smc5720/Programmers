import java.util.HashMap;

class Solution {
    public class Grade {
        int[][] cnt;
        HashMap<Character, Integer> charToInt;
        HashMap<Integer, Character> intToChar;

        public Grade() {
            cnt = new int[4][2];

            charToInt = new HashMap<>();
            intToChar = new HashMap<>();

            charToInt.put('R', 0);
            charToInt.put('T', 1);
            charToInt.put('C', 2);
            charToInt.put('F', 3);
            charToInt.put('J', 4);
            charToInt.put('M', 5);
            charToInt.put('A', 6);
            charToInt.put('N', 7);

            intToChar.put(0, 'R');
            intToChar.put(1, 'T');
            intToChar.put(2, 'C');
            intToChar.put(3, 'F');
            intToChar.put(4, 'J');
            intToChar.put(5, 'M');
            intToChar.put(6, 'A');
            intToChar.put(7, 'N');
        }

        public void addCount(char c, int score) {
            int i = charToInt.get(c);
            int a = i / 2;
            int b = i % 2;

            cnt[a][b] += score;
        }

        public String getGrade() {
            StringBuilder sb = new StringBuilder();

            for (int i = 0; i < 4; i++) {
                if (cnt[i][0] < cnt[i][1]) {
                    sb.append(intToChar.get(i * 2 + 1).toString());
                } else {
                    sb.append(intToChar.get(i * 2).toString());
                }
            }

            return sb.toString();
        }

        public void printCount() {
            for (int i = 0; i < 8; i++) {
                System.out.printf("%c : %d점\n", intToChar.get(i), cnt[i / 2][i % 2]);
            }

            System.out.println();
        }
    }

    public String solution(String[] survey, int[] choices) {
        Grade grade = new Grade();

        for (int i = 0; i < choices.length; i++) {
            if (choices[i] == 4) {
                continue;
            }

            String srv = survey[i];

            char a1 = srv.charAt(0);
            char a2 = srv.charAt(1);
            int score = choices[i] - 4;

            if (score < 0) {
                grade.addCount(a1, score * (-1));
            } else {
                grade.addCount(a2, score);
            }
        }

        return grade.getGrade();
    }
}