from geopy import Nominatim


def geocodeN(address):
    gps = Nominatim()
    location = gps.geocode(address)
    j = location.longitude
    w = location.latitude
    return j, w

print(geocodeN('白山'))

