import datetime
import argparse
from utils import deg2tile_num
from make_png import generate_image
from tile_servers import osm_tile_server, osm_sea_tile_server




def main():
    parser = argparse.ArgumentParser(description="generate png from OSM data")
    parser.add_argument("out", type=str, help="output file")

    parser.add_argument("xmin", type=float,  required=True)
    parser.add_argument("xmax", type=float, required=True)
    parser.add_argument("ymin", type=float, required=True)
    parser.add_argument("ymax", type=float, required=True)
    parser.add_argument("zoom", type=int, required=True)
    parser.add_argument("--tiles", type=bool, default=True)

    parser.add_argument("--server", type=int, default=0)
    parser.add_argument("--seamap", type=bool, default=True, help="Use OpenSeaMapLayer")
    parser.add_argument("--grid", type=bool, default=True, help="display a grid")
    parser.add_argument("--scale", type=bool, default=True, help="display a scale")

    args = parser.parse_args()

    if not args.tiles:
        xmin, ymin = int(args.xmin), int(args.ymin)
        xmax, ymax = int(args.xmax), int(args.ymax)
    else:
        xmin, ymin = deg2tile_num(args.xmin, args.ymin, args.zoom)
        xmax, ymax = deg2tile_num(args.xmax, args.ymax, args.zoom)

    if args.server >= len(osm_tile_server):
        pass

    layers = [ osm_tile_server[args.server]["url"] ]
    if args.seamap:
        layers.append(osm_sea_tile_server[0]["url"])

    if not args.out:
        now = datetime.datetime.now()
        outputFileName = "map%02d-%02d%02d%02d-%02d%02d.png" % (
        args.zoom, now.year % 100, now.month, now.day, now.hour, now.minute)
    else:
        output_file_name = args.out

    generate_image(args.zoom, xmin, ymin, xmax, ymax, layers, output_file_name)

if __name__ == "__main__":
    main()