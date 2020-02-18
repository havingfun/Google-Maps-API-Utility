def fetch_geolocation(query):
    import googlemaps
    import os
    from datetime import datetime

    gmaps = googlemaps.Client(key=os.environ['GOOGLE_MAPS_CREDENTIAL'])

    # Geocode an address
    geocode_result = gmaps.geocode(query)

    return geocode_result


def main():
    print(fetch_geolocation("BIG BAZAAR MUMBAI 400018"))


if __name__ == '__main__':
    main()
