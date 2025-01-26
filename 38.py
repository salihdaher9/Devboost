import csv


from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


ISRAEL_LAT, ISRAEL_LON = 31.5, 34.75


with open("cow.csv") as f, open("index.html", "w") as html:
    reader = csv.DictReader(f)
    print("<ul>", file=html)
    for d in reader:
        distance = haversine(float(d['lon']), float(d['lat']), ISRAEL_LON, ISRAEL_LAT)
        print(f"\t<li>{d['name']}: {distance:,.0f} km</li>", file=html)
    print("</ul>", file=html)