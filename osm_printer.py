import datetime
import argparse
from utils import deg2tile_num
from make_png import generate_image
from tile_servers import osm_tile_server, osm_overlay_tile_server, print_index2osm_tile_server, \
    print_index2osm_overlay_tile_server


class _PrintServersAction(argparse.Action):

    def __init__(self,
                 option_strings,
                 dest=argparse.SUPPRESS,
                 default=argparse.SUPPRESS,
                 help=None):
        super(_PrintServersAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        print_index2osm_tile_server()
        parser.exit()


class _PrintOverlayServersAction(argparse.Action):

    def __init__(self,
                 option_strings,
                 dest=argparse.SUPPRESS,
                 default=argparse.SUPPRESS,
                 help=None):
        super(_PrintOverlayServersAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        print_index2osm_overlay_tile_server()
        parser.exit()


def main():
    parser = argparse.ArgumentParser(description="generate png from OSM data", conflict_handler='resolve')
    parser.add_argument("xmin", type=float)
    parser.add_argument("xmax", type=float)
    parser.add_argument("ymin", type=float)
    parser.add_argument("ymax", type=float)
    parser.add_argument("zoom", type=int)
    parser.add_argument("--tiles", type=bool, default=True, help="False if coordinates are not tile number but degree")

    parser.add_argument("--out", type=str, help="output file")

    parser.add_argument("--server", type=int, default=0, choices=range(0, len(osm_tile_server)),
                        help="index of the base map server")
    parser.add_argument("--overlay", type=int, default=0, choices=range(1, len(osm_tile_server)),
                        help="index of an overlay server")
    parser.add_argument("--grid", type=bool, default=True, help="display a grid")
    parser.add_argument("--scalebar", type=bool, default=True, help="display a scale bar")

    parser.add_argument("--print-servers", action=_PrintServersAction,
                        help="display a list of all available OSM servers")
    parser.add_argument("--print-overlay-servers", action=_PrintOverlayServersAction,
                        help="display a list of all available OSM overlay servers")

    args = parser.parse_args()

    if args.tiles:
        xmin, ymin = int(args.xmin), int(args.ymin)
        xmax, ymax = int(args.xmax), int(args.ymax)
    else:
        xmin, ymin = deg2tile_num(args.xmin, args.ymin, args.zoom)
        xmax, ymax = deg2tile_num(args.xmax, args.ymax, args.zoom)

    if args.server >= len(osm_tile_server):
        # TODO error handling
        pass

    layers = [osm_tile_server[args.server]["url"]]
    if args.overlay > 0:
        layers.append(osm_overlay_tile_server[args.overlay]["url"])

    if not args.out:
        now = datetime.datetime.now()
        output_file_name = "map%02d-%02d%02d%02d-%02d%02d.png" % (
            args.zoom, now.year % 100, now.month, now.day, now.hour, now.minute)
    else:
        output_file_name = args.out

    generate_image(args.zoom, xmin, ymin, xmax, ymax, layers, output_file_name, args.scalebar, args.grid)


if __name__ == "__main__":
    main()
