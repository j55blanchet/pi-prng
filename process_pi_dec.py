"""
process_pi_dec.py

Utility to convert a randomy decimal ASCII file with
spaces and new lines into a similarly randomy binary
file (though not identical numbers) 


By Julien Blanchet and Thomas Kidder
"""

def strip_dec(src_file, out_file):
	with open(src_file) as sfile:
		with open(out_file, "w") as ofile:
			for line in sfile:
				newstr = ''.join(line.split())
				ofile.write(newstr)

def __convert_line(in_decimal_string, log=False):
	bytelist = []

	first_oct = None
	second_oct = None

	for char in in_decimal_string:
		num = int(char)

		if num < 8:
			if first_oct is None:
				first_oct = num % 8
				continue

			elif second_oct is None:
				second_oct = num % 8
				continue

			else:
				#map 4-7 to 1-3
				bite = num % 4 << 6
				bite += second_oct << 3
				bite += first_oct
				bytelist.append(bite)
				if log:
					print("{:0<2b} {:0>3b} {:0>3b} = {:0>8b}\n".format(num % 4, second_oct, first_oct, bite))
				first_oct = None
				second_oct = None

	return bytearray(bytelist)

def _random_decimal_to_random_binary(source, output, log=False):
	with open(source, "rt") as sfile:
		with open(output,"wb") as ofile:
			for line in sfile:
				mbytes = __convert_line(line, log)
				ofile.write(mbytes)


if __name__ == "__main__":
	import sys

	print (sys.argv)

	if not len(sys.argv) in (1,3,4):
		print("Bad Usage")
		sys.exit(-1)

	tfile = "test.tmp"

	if len(sys.argv) is 1:
		sfile = "test.dec"
		ofile = "test.bin"

	elif len(sys.argv) is 3:
		sfile = sys.argv[1]
		ofile = sys.argv[2]

	strip_dec(sfile, tfile)
	_random_decimal_to_random_binary(tfile, ofile, False)
