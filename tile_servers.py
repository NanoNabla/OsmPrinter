osm_tile_server = [
    {
        "name": "OpenStreetMap Standard tyle Server",
        "url": "https://tile.openstreetmap.org/!z/!x/!y.png",
        "rateLimit": 5,
    },
    {
        "name": "German fork of the Standard tile layer: openstreetmap.de",
        "url": "https://a.tile.openstreetmap.de/!z/!x/!y.png",
        "rateLimit": 5,
    },
    {
        "name": "OSM France",
        "url": "https://a.tile.openstreetmap.fr/osmfr/!z/!x/!y.png",
        "rateLimit": 1,
    },
    {
        "name": "Humanitarian map style",
        "url": "http://a.tile.openstreetmap.fr/hot/$!z/$!x/$!y.png",
        "rateLimit": 1,
    },
    {
        "name": "OpenTopoMap",
        "url": "https://a.tile.opentopomap.org/!z/!x/!y.png",
        "rateLimit": 2,
    },
    {
        "name": "Stamen Toner Black & White map",
        "url": "http://a.tile.stamen.com/toner/!z/!x/!y.png",
        "rateLimit": 5,
    },
    {
        "name": "Mapy.cz Base",
        "url": "https://m1.mapserver.mapy.cz/base-m/!z-!x-!y",
        "rateLimit": 10,
    },
    {
        "name": "Mapy.cz Turistic",
        "url": "https://m1.mapserver.mapy.cz/turist-m/!z-!x-!y",
        "rateLimit": 10,
    },
    {
        "name": "CyclOSM: OpenStreetMap-based bicycle map",
        "url": "https://a.tile-cyclosm.openstreetmap.fr/cyclosm/!z/!x/!y.png",
        "rateLimit": 1,
    }]

osm_overlay_tile_server = [
    {
        "name": "dummy",
        "url": "",
        "rateLimit": 5
    },
    {
        "name": "Standard OpenSeaMap tile server",
        "url": "http://tiles.openseamap.org/seamark/!z/!x/!y.png",
        "rateLimit": 5
    },
    {
        "name": "Waymarked Trails: Hiking routes",
        "url": "https://tile.waymarkedtrails.org/hiking/!z/!x/!y.png ",
        "rateLimit": 5
    },
    {
        "name": "Waymarked Trails: Cycling routes",
        "url": "https://tile.waymarkedtrails.org/cycling/!z/!x/!y.png ",
        "rateLimit": 5
    },
    {
        "name": "Waymarked Trails: Mountain bike routes",
        "url": "https://tile.waymarkedtrails.org/mtb/!z/!x/!y.png ",
        "rateLimit": 5
    },
    {
        "name": "Waymarked Trails: Riding routes",
        "url": "https://tile.waymarkedtrails.org/riding/!z/!x/!y.png ",
        "rateLimit": 5
    },
    {
        "name": "Waymarked Trails: Inline skating routes",
        "url": "https://tile.waymarkedtrails.org/skating/!z/!x/!y.png ",
        "rateLimit": 5
    },
    {
        "name": "Waymarked Trails: Slope routes",
        "url": "https://tile.waymarkedtrails.org/slopes/!z/!x/!y.png ",
        "rateLimit": 5
    },

    {
        "name": "OpenPtMap Transport map",
        "url": "http://www.openptmap.org/tiles/!z/!x/!y.png",
        "rateLimit": 5
    },
    {
        "name": "OpenRailwayMap: Railway infrastructure",
        "url": "http://a.tiles.openrailwaymap.org/standard/!z/!x/!y.png",
        "rateLimit": 5
    },
    {
        "name": "OpenRailwayMap: Railway maxspeed",
        "url": "http://a.tiles.openrailwaymap.org/maxspeed/!z/!x/!y.png",
        "rateLimit": 5
    },
    {
        "name": "OpenRailwayMap: Railway signals",
        "url": "http://a.tiles.openrailwaymap.org/signals/!z/!x/!y.png",
        "rateLimit": 5
    },
    {
        "name": "OpenFireMaps",
        "url": "http://www.openfiremap.de/hytiles/!z/!x/!y.png",
        "rateLimit": 5
    }
]

def print_index2osm_tile_server():
    for i in range(len(osm_tile_server)):
        print("{}: {}".format(i, osm_tile_server[i]['name']))

def print_index2osm_overlay_tile_server():
    for i in range(len(osm_overlay_tile_server)):
        print("{}: {}".format(i, osm_overlay_tile_server[i]['name']))