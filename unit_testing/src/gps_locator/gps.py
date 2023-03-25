import datetime
import re

from src.gps_locator.exceptions import CheckSumErrorException
import time


class Gps:
    def __init__(self, *args, raw=None, **kwargs):
        self.raw = raw
        self.parsed_data = None

        self.lat = 0.0
        self.lon = 0.0
        self.alt = 0.0
        self.heading = 0
        self.sat_num = 0
        self.time_stamp = None

        self.parsing_structure = {
            'time': 1,
            'lat': 2,
            'lat_heading': 3,
            'lon': 4,
            'lon_heading': 5,
            'fix_quality': 6,
            'sat_num': 7,
            'dilution': 8,
            'alt': 9
        }

    def convert_coordinates(self):
        lat = self.parsed_data[self.parsing_structure['lat']]
        lat_heading = self.parsed_data[self.parsing_structure['lat_heading']]
        lon = self.parsed_data[self.parsing_structure['lon']]
        lon_heading = self.parsed_data[self.parsing_structure['lon_heading']]

        r = re.match(r'^(\d+)(\d\d\.\d+)$', lat)
        d, m = r.groups()

        self.lat = (float(d) + float(m) / 60) * (1 if lat_heading == 'N' else -1)

        r = re.match(r'^(\d+)(\d\d\.\d+)$', lon)
        d, m = r.groups()

        self.lon = (float(d) + float(m) / 60) * (1 if lon_heading == 'E' else -1)

        print(self.lat)

    def convert_alt(self) -> None:
        self.alt = self.parsed_data[self.parsing_structure['alt']]
        if self.alt == 0:
            self.alt = 10

    def convert_time(self) -> None:
        raw_time = self.parsed_data[self.parsing_structure['time']]
        ms_s = raw_time[6:]
        ms = ms_s and int(float(ms_s) * 1000000) or 0

        self.time_stamp = datetime.time(
            hour=int(raw_time[0:2]),
            minute=int(raw_time[2:4]),
            second=int(raw_time[4:6]),
            microsecond=ms,
            tzinfo=datetime.timezone.utc
        )

    @classmethod
    def calc_checksum(cls, raw: str) -> bool:
        calc_checksum = 0
        current_checksum = hex(int(raw[len(raw) - 3:-1], 16))
        for i in raw[1:-6]:
            calc_checksum = calc_checksum ^ ord(i)
        if current_checksum == hex(calc_checksum):
            return True
        return False

    def parse_data(self):
        try:
            Gps.calc_checksum(self.raw)
            self.parsed_data = self.raw.split(',')
            self.convert_coordinates()
            self.convert_alt()
            self.convert_time()
        except CheckSumErrorException as e:
            print(e)
        except Exception as e:
            print(e)
