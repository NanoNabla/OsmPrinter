import math

# exact length of the equator (according to Wikipedia) is 40075.016686 km in WGS-84
equatorial_circumference = 40075.016686
tilesize = 256
attribution = 'Map data (c) OpenStreetMap'


def deg2tile_num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return (xtile, ytile)


def tile_num2deg(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return (lat_deg, lon_deg)


# https://wiki.openstreetmap.org/wiki/Zoom_levels#Distance_per_pixel_math
def km_per_pixel(zoom, latitude):
    return (equatorial_circumference * math.cos(latitude)) / (math.pow(2, zoom) * tilesize)


def pixel_per_km(zoom, latitude):
    return (math.pow(2, zoom) * tilesize) / (equatorial_circumference * math.cos(latitude))


def get_scale(resolution, dpi, latitude):
    return dpi * 1/0.0254 * resolution * math.cos(latitude)