// 3

import java.util.Scanner; // Import the scanner class


class Week6
{

	static int value;
 	static int count;



 	// 1
	public static boolean isprime(int number)
	{
		if (number <= 1)
		{
			return false;
		} else if (number % 2 == 0)

		{
			return false;
		} else 
		{
			return true;
		}
	}

	// 4
	public static void prime(int number)
	{
		int [] mylist = {};
		int index = 0;
		
		
		for (int i=1; i < 18; i++)
		{
			mylist[index] = i;
			index ++;
		}
		
		for (int list: mylist)
		{
			System.out.println("List: " + list);
		}
	}


}


public class Main
{
	public static void main(String [] args)
	{
		
		/*
		Scanner scanner = new Scanner(System.in);

		System.out.println("Enter your name: ");
		// read a full line of text
		String name = scanner.nextLine();


		System.out.println("Enter your age: ");
		// read an integer
		int age = scanner.nextInt();

		System.out.println("Hello : " + name + "! Your age: " +
		age + " years old.");

		// Close the scanner to free up resources
		scanner.close();

		*/
	

		Week6 program = new Week6();

		// boolean result = program.isprime(17);

		// System.out.println("Result: " + result);


		// 4
		program.prime(18);


	}
}