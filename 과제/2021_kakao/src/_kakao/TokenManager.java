package _kakao;

import java.io.*;

public class TokenManager {
	private static TokenManager instance = null;
	private String token = "";
	private String fileName = "D:\\Github\\코딩테스트\\프로그래머스\\과제\\2021_kakao\\src\\_kakao\\res\\token";

	public static TokenManager getInstance() {
		if (instance == null) {
			instance = new TokenManager();
		}

		return instance;
	}

	public String getToken() {
		return this.token;
	}

	public synchronized String createToken(int problemId) {
		String token = null;
		String response = Connection.getInstance().start(problemId);

		if (response.equals("400")) {
			System.out.println("400 :: Parameter Error");
		} else if (response.equals("401")) {
			System.out.println("401 :: X-auth-Token Header Error");
		} else if (response.equals("500")) {
			System.out.println("500 :: Server Error Please Contact");
		} else {
			saveTokenFile(response);
			token = response;
			response = "200";
		}

		this.token = token;
		return response;
	}

	private void saveTokenFile(String token) {
		try {
			BufferedWriter bw = new BufferedWriter(new FileWriter(fileName, false));
			bw.write(token);
			bw.flush();
			bw.close();
		} catch (IOException e) {
			System.out.println("?");
			e.printStackTrace();
		}
	}
}
