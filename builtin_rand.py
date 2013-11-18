

from random import *


if __name__ == "__main__":
	import sys, os
	num_bytes = 25000000
	ofilename = "builtin_rand.bin"

	if len(sys.argv) > 1:
		num_bytes = int(sys.argv[1])
	if len(sys.argv) > 2:
		ofilename = sys.argv[2]

	with open(ofilename, "wb") as ofile:
		i = 0
		while i < num_bytes:
			byte = os.urandom(10)
			#print(str(len(byte)) + "\t" + str(byte) + "\n")
			ofile.write(byte)

			if (i % 10000 == 0):
				percent = i / num_bytes
				print("{:>7.2%} {:>10,} / {:<10,}".format(percent, i, num_bytes))

			i += 10


