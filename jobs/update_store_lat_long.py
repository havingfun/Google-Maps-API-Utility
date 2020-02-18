# Read the data files
from maps import stores_geolocation
import csv
store_path = "../data/stores.csv"


def get_latitude_longitude(query):
    output_write = open("../data/output/store_results_output.txt", "a")
    print(query)
    try:
        store_geocode = stores_geolocation.fetch_geolocation(query)
        print(store_geocode)
        output_write.write(str(store_geocode))
        if len(store_geocode) > 0:
            print(
                store_geocode[0]["formatted_address"] + "\t" + str(store_geocode[0]["geometry"]["location"]["lat"]) + "\t" + str(store_geocode[0]["geometry"]["location"]["lng"])
            )
    except:
        error_message = "Error in fetching geolocation"
        output_write.write(error_message)
        print(error_message)
    output_write.close()


def main():
    with open(store_path, 'r', encoding='utf-8-sig') as f:
        csv_file = csv.reader(f)
        header = next(csv_file)
        stores = []
        for row in csv_file:
            store = {}
            for index, value in enumerate(row):
                store[header[index]] = value
            stores.append(store)
    for store in stores:
        get_latitude_longitude(store["format_desc"] + " " + store["city_desc"] + " " + store["store_zip"])


if __name__ == '__main__':
    main()