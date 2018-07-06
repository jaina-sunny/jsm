s = raw_input("enter a string ")
n = input("enter a key ")
st=""
def encrypt(s,n):
	st=""
	for i in range(0,len(s)):
		char=s[i]
		st=st+ chr((ord(char) + n - 97) % 26 + 97)
	return st
print "the result:" + encrypt(s,n)
	

