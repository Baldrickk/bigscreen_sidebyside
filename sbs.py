from PIL import Image
import sys

infile = sys.argv[1]
p1, p2 = infile.rsplit('.', 1)
outfile = '.'.join((p1, "edit", p2))

with Image.open(infile) as inf:
    iw, ih = inf.size
    boxl = (0, 0, iw / 2, ih)
    boxr = (iw / 2, 0, iw, ih)
    iml = inf.crop(boxl).resize((int(iw / 2), ih * 2))
    imr = inf.crop(boxr).resize((int(iw / 2), ih * 2))

    ow = iw * 2
    oh = ih * 2
    output = Image.new('RGB', (ow, oh), color='black')
    output.paste(iml, (int(ow * (1 / 8)), 0, int(ow * (3 / 8)), oh))
    output.paste(imr, (int(ow * (5 / 8)), 0, int(ow * (7 / 8)), oh))
    output.save(outfile)
