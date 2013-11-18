# pi-prng.py
# 
# Attempts to generate psuedo-random numbers by using the digits of π as a 
# source of numbers, and interpreting a given seed as criteria for selecting 
# output numbers from this sequence
#
# Julien Blanchet and Thomas Kidder
# Created: 11/1/2013

import time
import hashlib
from pistream import *

# 
"""Generate psuedo-random numbers using the digits of π as a 
source of numbers, and interpreting a given seed as criteria 
for selecting output numbers from this sequence
"""


PRNG_ADVANCE_MAGIC = "magicmagic"
PI_PRNG_ADVANCE_MODULO = 16

class PiPrng:
	"""Create a PiPrrg seeded with the start_pi'th digit of pi"""
	def __init__(self, seed=None):
		self.md5 = hashlib.md5()
		self.pi = PiStream()

		# we use hash function to generate seed from time when none specified
		if seed is None:
			time.clock() #for windows, in which this function returns value since previous call
			self.seed(time.clock())
		else:
			self.md5.update(str(seed))

		# note: we also want to go to a random position within the file!
		


	def seed(self, value):
		self.md5 = hashlib.md5()
		self.md5.update(str(value).encode())

	def getRandom(self, num_bytes=1):
		for i in range(num_bytes):
			self.md5.update(PRNG_ADVANCE_MAGIC.encode())

			# Use digest as method for determining skip distance
			offset = 1
			for byte in self.md5.digest():
				offset += byte
			offset %= PI_PRNG_ADVANCE_MODULO # Don't skip too much!
			offset = max(offset, 1) #make offset at least 1 (otherwise we have a loop!!) !

			self.pi.getBytes(offset) #read that many bytes, throw away
			return self.pi.getBytes(1)

	def __enter__(self):
		self.pi.__enter__()
	def __exit__(self, type, value, traceback):
		self.pi.__exit__(type, value, traceback)



# # Basic Test Program
# if __name__ == "__main__":
# 	import sys
# 	prng = PiPrng()
# 	with prng:

# 		seed = "Hello World!"
# 		if len(sys.argv) > 1:
# 			seed = sys.argv[1]
# 		prng.seed(seed)

# 		for i in range(10):
# 			print(prng.getRandom())


# Generating a long randomy output
if __name__ == "__main__":
	import sys

	ofilename = "output.bin"
	totalbytes = 25000000    # 25m bytes

	if len(sys.argv) > 1:
		ofilename = sys.argv[1]
	if len(sys.argv) > 2:
		totalbytes = int(sys.argv[2])

	with open(ofilename, "wb") as ofile:
		prng = PiPrng()
		with prng:
			i = 0
			while(i < totalbytes): 
				if (i % 10000 == 0):
					percent = i / totalbytes
					print("{:>7.2%} {:>10,} / {:<10,}".format(percent, i, totalbytes))

				ofile.write(prng.getRandom(1))
				i += 1