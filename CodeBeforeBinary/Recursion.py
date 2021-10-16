#This code outputs the first 100 digits of the fibnonacci sequence using recursion
def Fibonacci(n): #Takes a parameter n as the nth term of the fibonacci sequence
	if n==0: 
		return(0) #0 is the first term
	elif n==1: 
		return(1)	##base cases #1 is the second term
	else: 
		return Fibonacci(n-1) + Fibonacci(n-2) #This is the recursive part where the 3rd term is 0 + 1 and hence 4th term is 1 + 1

for i in range(1,100):
    print(Fibonacci(i))