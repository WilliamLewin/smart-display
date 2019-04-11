import geopy.distance

coords_1 = (59.243615, 17.574428)
coords_2 = (59.243705, 17.574502)

print geopy.distance.vincenty(coords_1, coords_2).m
