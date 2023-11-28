package day03;

public class Vehicle {
	
	int	cnt_wheel = 4;
	
	public void funk(int cnt) {
		cnt_wheel -= cnt;
	}
	
	public static void main(String[] args) {
		Vehicle veh = new Vehicle();
		System.out.println(veh.cnt_wheel);
		veh.funk(2);
		System.out.println(veh.cnt_wheel);
	}
	
	
}
