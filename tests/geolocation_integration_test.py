import pytest
from modules.geolocation import geolocation


def test_run_locator():
    # This test data is bogus, pls get me some realistic data
    mock_camera_euler = {
        'x': 0,
        'y': 340,
        'z': 0
    }
    mock_plane_euler = {
        'x': 0,
        'y': 340,
        'z': 0
    }
    mock_gps = [0, 0]
    mock_telemetry = {
        "eulerAnglesOfPlane": mock_plane_euler,
        "eulerAnglesOfCamera": mock_camera_euler,
        "gpsCoordinates": mock_gps
    }

    mock_coordinates = [[0, 0]]

    locator = geolocation.Geolocation()
    # Will be filled when I have  better test data
