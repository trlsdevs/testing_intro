from inspect import signature
from unit_testing.src.gps_locator.gps import Gps
import unittest
import pytest
import logging
from tests.fixtures import custom_requests


class TestGps(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logging.info('>>>>>>> CLASS SUITE SETUP: %s <<<<<<<', cls.__class__.__name__)
        raw_data = '$GPGGA,180216.563,3246.477,N,03501.409,E,1,12,1.0,0.0,M,0.0,M,,*6F'
        cls.gps_data: Gps = Gps(raw=raw_data)
        cls.gps_data.parse_raw_data()

    @classmethod
    def tearDownClass(cls) -> None:
        logging.info('>>>>>>> CLASS SUITE TEARDOWN: %s <<<<<<<', cls.__class__.__name__)

    def tearDown(self) -> None:
        logging.info('>>>>>>> TEST TEARDOWN: %s <<<<<<<', self.__class__.__name__)

    def setUp(self) -> None:
        logging.info('>>>>>>> TEST SETUP: %s <<<<<<<', self.__class__.__name__)

    def test_coords_conversion(self):
        self.gps_data.convert_coordinates()

        assert self.gps_data.lat == 32.77461666666667
        assert self.gps_data.lon == 35.02348333333333

    def test_alt(self):
        self.gps_data.convert_alt()

        assert self.gps_data.alt == 10

    def test_time_conversion(self):
        self.gps_data.convert_time()

        assert self.gps_data.time_stamp.hour == 18
        assert self.gps_data.time_stamp.minute == 2
        assert self.gps_data.time_stamp.second == 16
        assert self.gps_data.time_stamp.microsecond == 563000

    @pytest.mark.timeout(4)
    def test_checksum_calc_time(self):
        self.gps_data.calc_checksum(self.gps_data.raw, if_timeout=True)

    def test_send_data(self):
        res = self.gps_data.send_data()
        assert res is True
