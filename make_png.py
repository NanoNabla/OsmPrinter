#!/usr/bin/env python

import io, urllib.request, time, re, random
from PIL import Image, ImageDraw
from utils import tilesize, attribution, tile_num2deg, pixel_per_km, degree2min_str


# TODO do not use constantly 1km, resize it depending on zoom level
def draw_scalebar(draw, xmin, ymax, ysize, zoom):
    colormap = [(0, 0, 0), (255, 0, 0)]
    line_width = 5
    ########
    ypos = ysize * tilesize - 50
    xpos_min = 5
    lat, _ = tile_num2deg(xmin, ymax, zoom)
    xpos_len = abs(pixel_per_km(zoom, lat))

    for i in range(5):
        draw.line([(xpos_min + xpos_len * i, ypos), (xpos_min + ((i + 1) * xpos_len), ypos)], fill=colormap[i % 2],
                  width=line_width)
    draw.text((xpos_min + 5, ypos + line_width + 5), "1km", (0, 0, 0))


def draw_grid(draw, xmin, ymin, xsize, ysize, zoom):
    for x in range(0, xsize):
        xpos = x * tilesize
        draw.line([(xpos, 0), (xpos, (ymin + ysize) * tilesize)], fill=(0, 0, 0), width=1)
        _, long = tile_num2deg(xmin + x, 0, zoom)
        draw.text((xpos, 5), degree2min_str(long), (0, 0, 0))
    for y in range(0, ysize):
        ypos = y * tilesize
        draw.line([(0, ypos), ((xmin + xsize) * tilesize, ypos)], fill=(0, 0, 0), width=1)
        lat, _ = tile_num2deg(0, ymin + y, zoom)
        draw.text((5, ypos), degree2min_str(lat), (0, 0, 0))


def draw_credits(draw, ysize):
    draw.text((5, ysize * tilesize - 15), attribution, (0, 0, 0))


def generate_image(zoom, xmin, ymin, xmax, ymax, layers, output_file_name="map.png", grid=False):
    xsize = xmax - xmin + 1
    ysize = ymax - ymin + 1

    resultImage = Image.new("RGBA", (xsize * tilesize, ysize * tilesize), (0, 0, 0, 0))
    counter = 0
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
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
                resultImage.paste(image, ((x - xmin) * tilesize, (y - ymin) * tilesize), image.convert("RGBA"))
                counter += 1
                if counter == 10:
                    # time.sleep(2);
                    counter = 0

    draw = ImageDraw.Draw(resultImage)
    draw_credits(draw, ysize)
    draw_scalebar(draw, xmin, ymax, ysize, zoom)
    if grid:
        draw_grid(draw, xmin, ymin, xsize, ysize, zoom)
    del draw

    resultImage.save(output_file_name)
    print("file {} written".format(output_file_name))
