def fact(num):
	num=8
	if num==0:
		return 1
	else:
		facto=(num*fact(num-1))
		return facto
	num=int(raw_input())
	print fact(num)



