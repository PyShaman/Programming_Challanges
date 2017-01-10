# Task 28 Fibonacci sequence from Pro/g/ramming Challanges [Made by Anonymous in January 2015]


def fibonacci_recursion(n):
	a, b = 0, 1
	for i in range(0,n):
		a, b = b, a + b
		print(a)
	
numbers_in_fibonacci_sequence = int(input("How many numbers in Fibonacci sequence you want to see: "))
print(fibonacci_recursion(numbers_in_fibonacci_sequence))