n=int(input())
h_tri=n//2
h_grap_heart=n//2-2
w_square=n*2+1
############### 2 triangle
for i in range(h_tri):
	if i == h_tri-1:
	    ######### base of 1st triangle
		for j in range(n):
			print("#", end='') #### print without new line pattern
		######### gap between triangle
		print(".", end='')
		######### base of 2nd triangle
		for j in range(n):
			print("#", end='')
		### new line
		print()
	else:
		h_tri_free_space=h_tri-1-i
		if h_tri_free_space > 0 :
		######### 1st triangle
			for j in range(h_tri_free_space):
				print(".", end='')
			for j in range(n-(2*h_tri_free_space)):
				print("#", end='')
			for j in range(h_tri_free_space):
				print(".", end='')
		######### gap between triangle
			print(".", end='')
		######### 2nd triangle
			for j in range(h_tri_free_space):
				print(".", end='')
			for j in range(n-(2*h_tri_free_space)):
				print("#", end='')
			for j in range(h_tri_free_space):
				print(".", end='')
		### new line
			print()
		else:
			for j in range(n):
				print("#", end='')
			print(".", end='')
			for j in range(n):
				print("#", end='')
		### new line
			print()
############# grap between 2 triangle and clockwise triangle
for i in range(h_grap_heart):
	for j in range(w_square):
		print("#", end='')
	### new line
	print()
############ clockwise triangle
for i in range((w_square//2)+1):
	for j in range(i):
		print(".", end='')
	for j in range(w_square-(i)*2):
		print("#", end='')
	for j in range(i):
		print(".", end='')
	### new line
	print()