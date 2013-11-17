pi-prng
=======

By Julien Blanchet and Thomas Kidder

Notes: 
- To run diehard test suite, we need to have a binary input.
	> we do the following to convert our pi file:
		* pi10m.txt contains the first 10m digits of pi, divided into 10-digit segments  
		* pi10m.dec contains the above file, stripped of whitespace and mapped to binary (keeping randomness, but not exact values)
		* This conversion process is done by process_pi.xtx
- pi-prng.py is an implmentation of a PRNG that uses this file to extend the entropy of the input
	> How it works:
		* Keeps state that includes:
			1) md5 hash that is updated with magic string each iterations
			2) position within a "pistream" file, a source of precompputed randomy numbers
		* Whenever random byte is requested, it:
			1) updates the hash
			2) advances in pistream file by a number computed from this hash, modulo a certain value (to prevent excessive skipping)
	> Noteworthy considerations:
		* The pistream class loops to the beginning of the randomy source file when it reaches the end. 
			1) How will this affect randomness measurements? 
			2) How much does this depend on the size of the source file?
			3) Is there a ratio of loops over the file where randomness tests significantly degrade?
				- Does it degrade the very first repetition?
		* How does the modulo threshold affect randomness of outputs?
			- How does it affect performance?