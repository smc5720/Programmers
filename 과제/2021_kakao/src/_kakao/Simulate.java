package _kakao;

public class Simulate {
	private String status;
	private int time;
	private String totalDistance;
	private int failRequest;

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public int getTime() {
		return time;
	}

	public void setTime(int time) {
		this.time = time;
	}

	public String getTotalDistance() {
		return totalDistance;
	}

	public void setTotalDistance(String totalDistance) {
		this.totalDistance = totalDistance;
	}

	public int getFailRequest() {
		return failRequest;
	}

	public void setFailRequest(int failRequest) {
		this.failRequest = failRequest;
	}

	@Override
	public String toString() {
		return "status : " + status + " time : " + time + " totalDistance : " + totalDistance + " failRequest : "
				+ failRequest;
	}
}
