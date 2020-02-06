from PIL import Image
import sys

for infile in sys.argv[1:]:
	p1, p2 = infile.rsplit('.', 1)
	outfile = '.'.join((p1, "edit", p2))

	with Image.open(infile) as inf:
		iw, ih = inf.size
		iw = iw // 2
		
		# determine canvas size
		ch = max(ih, iw * 9.0 / 16)
		cw = int(2* ih * 16 / 9.0)
		ch = int(2 * ch)
		canvas = Image.new('RGB', (cw, ch), color='black')
		
		boxl = (0, 0, iw, ih)
		boxr = (iw, 0, iw * 2, ih)
		iml = inf.crop(boxl).resize((iw, ih * 2))
		imr = inf.crop(boxr).resize((iw, ih * 2))

		ow, oh = iml.size
		canvas.paste(iml, ((cw * 1) // 4 - ow // 2, ch // 2 - oh // 2, (cw * 1) // 4 + ow // 2, ch // 2 + oh // 2))
		canvas.paste(imr, ((cw * 3) // 4 - ow // 2, ch // 2 - oh // 2, (cw * 3) // 4 + ow // 2, ch // 2 + oh // 2))
		canvas.save(outfile)
