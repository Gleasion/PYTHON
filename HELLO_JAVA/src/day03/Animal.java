package day03;

public class Animal {
	int cnt_hair = 1000;
	
	public void tsShampoo() {
		cnt_hair += 100;
	}
	
	public static void main(String[] args) {
		Animal ani = new Animal();
		System.out.println("b" + ani.cnt_hair);
		ani.tsShampoo();
		System.out.println("b" + ani.cnt_hair);
		
	}
	
}
