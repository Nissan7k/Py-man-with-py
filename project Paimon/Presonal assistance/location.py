import geocoder

def get_current_location():
    g = geocoder.ip('me')
    return g.latlng

