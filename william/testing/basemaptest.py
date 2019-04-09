#TEST
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="test")
location = geolocator.reverse("59.40690003, 17.95646688")
print(location.address)
