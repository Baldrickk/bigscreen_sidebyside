from PIL import Image
import sys

infile = sys.argv[1]
p1, p2 = infile.rsplit('.', 1)
outfile = '.'.join((p1, "edit", p2))

with Image.open(infile) as inf:
    iw, ih = inf.size
    iw = iw // 2
    boxl = (0, 0, iw, ih)
    boxr = (iw, 0, iw * 2, ih)
    imr = inf.crop(boxr).resize((iw, ih * 2))
    iml = inf.crop(boxl).resize((iw, ih * 2))

    ow = 2 * max(2 * iw, int(ih * 11.0 / 9.0))
    oh = 2 * max(ih, int(iw * 9.0 / 11.0))
    
    output = Image.new('RGB', (ow, oh), color='black')
    imlw, imlh = iml.size
    imrw, imrh = imr.size
    output.paste(iml, ((ow * 1) // 4 - imlw // 2, oh // 2 - imlh // 2, (ow * 1) // 4 + imlw // 2, oh // 2 + imlh // 2))
    output.paste(imr, ((ow * 3) // 4 - imrw // 2, oh // 2 - imrh // 2, (ow * 3) // 4 + imrw // 2, oh // 2 + imrh // 2))
    output.save(outfile)
