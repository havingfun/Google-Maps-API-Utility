def fetch_nearby(query, location, types, rank_by='distance', language='en-IN'):
    import googlemaps
    import os

    gmaps = googlemaps.Client(key=os.environ['GOOGLE_MAPS_CREDENTIAL'])

    nearby_places = gmaps.places_nearby(
        location=location, keyword=query,
        language=language, rank_by=rank_by,
        type=types
    )

    return nearby_places


def main():
    fetch_nearby("D Mart", (19.0996465, 72.9155826), ['grocery'])


if __name__ == "__main__":
    main()