def fetch_geolocation(query):
    import googlemaps
    import os

    gmaps = googlemaps.Client(key=os.environ['GOOGLE_MAPS_CREDENTIAL'])

    # Geocode an address
    geocode_result = gmaps.geocode(query)

    return geocode_result


def main():
    print(fetch_geolocation("Mustafa Singapore"))


if __name__ == '__main__':
    main()
