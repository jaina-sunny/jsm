import sys
def path(m,n):
		if(m == 1 or n == 1):
			return 1;
		else:	
			return  path(m-1, n) + path(m, n-1);
m=input("enter row")
n=input("enter column")
print(path(m,n))
	