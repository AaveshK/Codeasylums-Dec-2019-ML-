T=int(input())
for i in range(T):
	n=int(input())
	k = 3 * ((n * (n + 1))/2) - n;
	k = k % 1000007;
	print(int(k))
