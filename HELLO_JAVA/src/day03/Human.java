package day03;

public class Human extends Animal {
	
	boolean flag_dev = false;
	
	public void principle_voice() {
		flag_dev = true;
	}
	
	public static void main(String[] args) {
		Human hum = new Human();
		System.out.println(hum.flag_dev);
		System.out.println(hum.cnt_hair);
		hum.principle_voice();
		hum.tsShampoo();
		System.out.println(hum.flag_dev);
		System.out.println(hum.cnt_hair);
	}
	
}
