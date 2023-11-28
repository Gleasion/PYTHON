package day03;

public class MyMethod {
	public static int add(int a, int b) {
		return a+b;
	}
	
	public static int minus(int a, int b) {
		return a-b;
	}
	
	public static int multiply(int a, int b) {
		return a*b;
	}
	
	public static void main(String[] args) {
		int sum = add(4, 5);
		int min = minus(4, 5);
		int mul = multiply(4, 5);
		
		
		System.out.println("sum: " + sum);
		System.out.println("min: " + min);
		System.out.println("mul: " + mul);
		
	}
	
}
