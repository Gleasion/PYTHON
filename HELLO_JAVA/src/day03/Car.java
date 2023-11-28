package day03;

public class Car extends Vehicle{
	
	int volume_speaker = 20;
	
	public void turnRight(int cnt) {
		volume_speaker += cnt;
	}
	
	public void turnLeft(int cnt) {
		volume_speaker -= cnt;
	}
	
	public static void main(String[] args) {
		Car c = new Car();
		System.out.println(c.cnt_wheel);
		System.out.println(c.volume_speaker);
		c.funk(1);
		c.turnRight(5);
		System.out.println(c.cnt_wheel);
		System.out.println(c.volume_speaker);
	}
}
