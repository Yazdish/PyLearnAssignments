def generate_rug(n):
	ret = []
	
	for i in range(n):
		ret.append([0] * n)
		for j in range(n):
			ret[i][j] = max(abs(n//2 - i),abs(n//2 - j))
	
	return ret

print(generate_rug(7))
