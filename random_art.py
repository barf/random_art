#!/usr/bin/env python3
#
# random_art.py by barf <stuart@macintosh.nz>
#

import rdrand
from PIL import Image

if __name__=='__main__':
	rdrando = rdrand.RdRandom()

	mode = "RGB" # “L”, “RGBX”, “RGBA”, “CMYK”
	size = (256,256)
	img = Image.new(mode, size, 0)
	pixels = img.load()

	for i in range(img.size[0]):
		for j in range(img.size[1]):
			r = int.from_bytes(rdrando.getrandbytes(1), "big")
			g = int.from_bytes(rdrando.getrandbytes(1), "big")
			b = int.from_bytes(rdrando.getrandbytes(1), "big")
			pixels[i,j] = (r, g, b)

	# for i in range(img.size[0]):
	# 	for j in range(img.size[1]):
	# 		r = int.from_bytes(rdrando.getrandbytes(1), "big")
	# 		g = int.from_bytes(rdrando.getrandbytes(1), "big")
	# 		b = int.from_bytes(rdrando.getrandbytes(1), "big")
	# 		pixels[int.from_bytes(rdrando.getrandbytes(1), "big"), int.from_bytes(rdrando.getrandbytes(1), "big")] = (r, g, b)

	img.show()