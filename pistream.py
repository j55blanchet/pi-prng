"""pistream.py

Reads a random file in a loop to represent ongoing data


"""

class PiStream:
	def __init__(self, filename="shortpi.bin"):
		self.mfile = None
		self.filename = filename
		self.pos = 0
		self.loopcount = 0


	def seek(self, offset):
		if self.mfile is not None:
			self.mfile.seek(offset)

	def __enter__(self):
		self.mfile = open(self.filename, "rb")

	def __exit__(self, type, value, traceback):
		try:
			self.mfile.close()
		except Exception as ex:
			print(ex)

	def set_position(self, percent):
		pass

	def getBytes(self, num_bytes=1):
		if self.mfile is not None:
			bytes = self.mfile.read(num_bytes)

			# At end of file? Go back to beginning!
			while(len(bytes) < num_bytes):
				self.seek(0)
				self.loopcount += 1
				bytes = bytes + self.mfile.read(num_bytes - len(bytes))
			return bytes

		else:
			raise Exception("PiStream must be used in a with bock")



if __name__ == "__main__":
	mpi = PiStream()
	with mpi:
		print(mpi.getBytes(10))