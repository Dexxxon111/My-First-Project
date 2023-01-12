a=int(input("Enter Any Number for palindrome:"))
temp=a
rev=0
while(a>0):
	dig=a%10
	rev=rev*10+dig
	a=a//10

if(temp==rev):
	print("Numberis Palindrome")
else:	
	print(" is not a Palindrome")
