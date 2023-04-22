limit = 1500

print("[myheader]")
print("mykey=[")
for i in range(1,limit):
	print("\t\"", end="")
	for i in range(0,i):
		print("a", end="")

	if i != limit-2:
		print("\",")
	else:
		print("\"")
		print("]")