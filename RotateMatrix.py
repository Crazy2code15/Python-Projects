#Rotate matrix 90 degree (clockwise)
#Defining function
def rotateMatrix(M):
	N = len(M[0])
	for i in range(N // 2):
		for j in range(i, N - i - 1):
			temp = M[i][j]
			M[i][j] = M[N - 1 - j][i]
			M[N - 1 - j][i] = M[N - 1 - i][N - 1 - j]
			M[N - 1 - i][N - 1 - j] = M[j][N - 1 - i]
			M[j][N - 1 - i] = temp


def printMatrix(M):
	N = len(M[0])
	for i in range(N):
		print(M[i])

#Calling function
A = [[11, 2, 14, 40],
	[55, 2, 6, 18],
	[9, 1, 11, 54],
	[3, 22, 15, 9]]
rotateMatrix(A)