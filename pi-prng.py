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



def __calculate_pi(digit):
	pass

"""Generate psuedo-random numbers using the digits of π as a 
source of numbers, and interpreting a given seed as criteria 
for selecting output numbers from this sequence
"""
class PiPrng:
	"""Create a PiPrrg seeded with the start_pi'th digit of pi"""
	def __init__(self, start_pi=None):

		# we use hash function to generate seed from time when none specified
		if start_pi is None:
			m_md5 = hashlib.md5()
			time_str = str(time.time())
			time_bytes = time_str.encode()
			m_md5.update(time_bytes)
			self.pi_index = int.from_bytes(m_md5.digest(), 'big')
		else:
			self.pi_index = startPi

	def advance():
		pass


if __name__ == "__main__":
	prng = PiPrng()
	print(prng.pi_index)


del __calculate_pi