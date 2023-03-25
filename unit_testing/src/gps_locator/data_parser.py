from gps import Gps

gps_data = []


def import_data_from_file():
    with open('./coords.nmea', 'r') as f:
        for raw in f.readlines():
            if raw.startswith('$GPGGA'):
                gps_data.append(Gps(raw=raw).parse_data())


import_data_from_file()
