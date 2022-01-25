#!/usr/bin/env python

import io, urllib.request, time, re, random
from PIL import Image, ImageDraw
from utils import tilesize, attribution

def generate_image(zoom, xmin, ymin, xmax, ymax, layers, output_file_name="map.png"):
	xsize = xmax - xmin + 1
	ysize = ymax - ymin + 1

	resultImage = Image.new("RGBA", (xsize * tilesize, ysize * tilesize), (0,0,0,0))
	counter = 0
	for x in range(xmin, xmax+1):
		for y in range(ymin, ymax+1):
			for layer in layers:
				url = layer.replace("!x", str(x)).replace("!y", str(y)).replace("!z", str(zoom))
				match = re.search("{([a-z0-9]+)}", url)
				if match:
					url = url.replace(match.group(0), random.choice(match.group(1)))
				print(url, "... ");
				try:
					req = urllib.request.Request(url, headers={'User-Agent': 'osm_Printer'})
					tile = urllib.request.urlopen(req).read()
				except Exception as e:
					print("Error", e)
					continue;
				image = Image.open(io.BytesIO(tile))
				resultImage.paste(image, ((x-xmin)*tilesize, (y-ymin)*tilesize), image.convert("RGBA"))
				counter += 1
				if counter == 10:
					time.sleep(2);
					counter = 0

	draw = ImageDraw.Draw(resultImage)
	draw.text((5, ysize*tilesize-15), attribution, (0,0,0))
	del draw

	resultImage.save(output_file_name)
