import pytest

from src.gps_locator.exceptions import CheckSumErrorException
from src.gps_locator.gps import Gps


@pytest.mark.parametrize('raw_data', [
    '$GPGGA,180217.563,3246.509,N,03501.338,E,1,12,1.0,0.0,M,0.0,M,,*63',
    '$GPGGA,180219.563,3246.624,N,03501.177,E,1,12,1.0,0.0,M,0.0,M,,*68',
    '$GPGGA,180220.563,3246.666,N,03501.065,E,1,12,1.0,0.0,M,0.0,M,,*66',
    '$GPGGA,180221.563,3246.689,N,03500.991,E,1,12,1.0,0.0,M,0.0,M,,*65',
    '$GPGGA,180222.563,3246.704,N,03500.947,E,1,12,1.0,0.0,M,0.0,M,,*69',
])
def test_multi_messages(raw_data):
    gps: Gps = Gps(raw=raw_data)
    gps.parse_raw_data()


def test_alt():
    raw = '$GPGGA,180219.563,3246.624,N,03501.177,E,1,12,1.0,0.0,M,0.0,M,,*68'
    gps: Gps = Gps(raw=raw)
    gps.parse_raw_data()

    gps.convert_alt()
    assert gps.alt > 1


def test_coord_conversion():
    raw = '$GPGGA,180219.563,3246.624,N,03501.177,E,1,12,1.0,0.0,M,0.0,M,,*68'
    gps: Gps = Gps(raw=raw)
    gps.parse_raw_data()

    gps.convert_coordinates()
    assert gps.lat == 32.77706666666667


def test_time_conversion():
    raw = '$GPGGA,180219.563,3246.624,N,03501.177,E,1,12,1.0,0.0,M,0.0,M,,*68'
    gps: Gps = Gps(raw=raw)
    gps.parse_raw_data()

    gps.convert_time()

    assert gps.time_stamp.hour == 18
    assert gps.time_stamp.minute == 2
    assert gps.time_stamp.second == 19


def test_checksum_error():
    raw = '$GPGGA,180219.563,3246.624,N,03501.177,E,1,12,1.0,0.0,M,0.0,M,,*61'
    gps: Gps = Gps(raw=raw)
    with pytest.raises(CheckSumErrorException) as exc:
        gps.parse_raw_data()
    assert exc.type == CheckSumErrorException


@pytest.mark.skip('broken test')
def test_broken_test():
    pass
