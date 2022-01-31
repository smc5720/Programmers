package _kakao;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class Connection {
	private static Connection instance = null;
	private static String connType = "Content-Type";
	private static String connJson = "application/json";
	private static String connAuth = "Authorization";

	public static Connection getInstance() {
		if (instance == null) {
			instance = new Connection();
		}

		return instance;
	}

	public JSONObject trucks() {
		HttpURLConnection conn = null;
		JSONObject responseJson = null;

		try {
			URL url = new URL(Global.HOST_URL + Global.GET_TRUCKS);
			conn = (HttpURLConnection) url.openConnection();

			conn.setRequestMethod("GET");
			conn.setRequestProperty(connAuth, TokenManager.getInstance().getToken());
			conn.setRequestProperty(connType, connJson);

			int responseCode = conn.getResponseCode();

			if (responseCode == 400) {
				System.out.println("400 :: Can't");
			} else if (responseCode == 401) {
				System.out.println("401 :: X-auth-Token Header Error");
			} else if (responseCode == 500) {
				System.out.println("500 :: Server Error Please Contact");
			} else {
				// Success
				BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
				StringBuilder sb = new StringBuilder();
				String line = "";

				while ((line = br.readLine()) != null) {
					sb.append(line);
				}

				responseJson = new JSONObject(sb.toString());
			}
		} catch (MalformedURLException e) {
			e.printStackTrace();
		} catch (IOException e) {
			System.out.println("openConnection Error");
			e.printStackTrace();
		} catch (JSONException e) {
			System.out.println("Not JSON Format response");
			e.printStackTrace();
		}

		return responseJson;
	}

	public JSONObject simulate(JSONArray commandArrays) {
		HttpURLConnection conn = null;
		JSONObject responseJson = null;

		try {
			URL url = new URL(Global.HOST_URL + Global.PUT_SIMULATE);
			conn = (HttpURLConnection) url.openConnection();

			conn.setRequestMethod("PUT");
			conn.setRequestProperty(connAuth, TokenManager.getInstance().getToken());
			conn.setRequestProperty(connType, connJson);
			conn.setDoOutput(true);
			conn.setDoInput(true);

			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(conn.getOutputStream()));
			JSONObject commands = new JSONObject();
			commands.put("commands", commandArrays);

			bw.write(commands.toString());
			bw.flush();
			bw.close();

			int responseCode = conn.getResponseCode();

			if (responseCode == 400) {
				System.out.println("400 :: Can't");
			} else if (responseCode == 401) {
				System.out.println("401 :: X-auth-Token Header Error");
			} else if (responseCode == 500) {
				System.out.println("500 :: Server Error Please Contact");
			} else {
				// Success
				BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
				StringBuilder sb = new StringBuilder();
				String line = "";

				while ((line = br.readLine()) != null) {
					sb.append(line);
				}

				responseJson = new JSONObject(sb.toString());
			}
		} catch (MalformedURLException e) {
			e.printStackTrace();
		} catch (IOException e) {
			System.out.println("openConnection Error");
			e.printStackTrace();
		} catch (JSONException e) {
			System.out.println("Not JSON Format response");
			e.printStackTrace();
		}

		return responseJson;
	}

	public JSONObject locations() {
		HttpURLConnection conn = null;
		JSONObject responseJson = null;

		try {
			URL url = new URL(Global.HOST_URL + Global.GET_LOCATIONS);
			conn = (HttpURLConnection) url.openConnection();

			conn.setRequestMethod("GET");
			conn.setRequestProperty(connAuth, TokenManager.getInstance().getToken());
			conn.setRequestProperty(connType, connJson);

			int responseCode = conn.getResponseCode();

			if (responseCode == 400) {
				System.out.println("400 :: Can't");
			} else if (responseCode == 401) {
				System.out.println("401 :: X-auth-Token Header Error");
			} else if (responseCode == 500) {
				System.out.println("500 :: Server Error Please Contact");
			} else {
				// Success
				BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
				StringBuilder sb = new StringBuilder();
				String line = "";

				while ((line = br.readLine()) != null) {
					sb.append(line);
				}

				responseJson = new JSONObject(sb.toString());
			}
		} catch (MalformedURLException e) {
			e.printStackTrace();
		} catch (IOException e) {
			System.out.println("openConnection Error");
			e.printStackTrace();
		} catch (JSONException e) {
			System.out.println("Not JSON Format response");
			e.printStackTrace();
		}

		return responseJson;
	}

	public JSONObject score() {
		HttpURLConnection conn = null;
		JSONObject responseJson = null;

		try {
			URL url = new URL(Global.HOST_URL + Global.GET_SCORE);
			conn = (HttpURLConnection) url.openConnection();

			conn.setRequestMethod("GET");
			conn.setRequestProperty(connAuth, TokenManager.getInstance().getToken());
			conn.setRequestProperty(connType, connJson);

			int responseCode = conn.getResponseCode();

			if (responseCode == 400) {
				System.out.println("400 :: Can't");
			} else if (responseCode == 401) {
				System.out.println("401 :: X-auth-Token Header Error");
			} else if (responseCode == 500) {
				System.out.println("500 :: Server Error Please Contact");
			} else {
				// Success
				BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
				StringBuilder sb = new StringBuilder();
				String line = "";

				while ((line = br.readLine()) != null) {
					sb.append(line);
				}

				responseJson = new JSONObject(sb.toString());
			}
		} catch (MalformedURLException e) {
			e.printStackTrace();
		} catch (IOException e) {
			System.out.println("openConnection Error");
			e.printStackTrace();
		} catch (JSONException e) {
			System.out.println("Not JSON Format response");
			e.printStackTrace();
		}

		return responseJson;
	}

	public String start(int problemId) {
		HttpURLConnection conn = null;
		JSONObject responseJson = null;
		String response = null;

		try {
			URL url = new URL(Global.HOST_URL + Global.POST_START + "?problem=" + problemId);
			conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("POST");
			conn.setRequestProperty("X-auth-Token", Global.X_AUTH_TOKEN);
			conn.setRequestProperty(connType, connJson);

			int responseCode = conn.getResponseCode();

			if (responseCode == 200) {
				// Success
				BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
				StringBuilder sb = new StringBuilder();
				String line = "";

				while ((line = br.readLine()) != null) {
					sb.append(line);
				}

				responseJson = new JSONObject(sb.toString());
				response = responseJson.getString("auth_key");
			} else {
				response = String.valueOf(responseCode);
			}
		} catch (ProtocolException e) {
			e.printStackTrace();
		} catch (MalformedURLException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

		System.out.println("response = " + response);
		return response;
	}
}
