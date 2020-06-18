import pytest
from main import get_temperature
from unittest.mock import Mock, patch

test_array = [
    (-14.235004,-51.92528,62,16),
    (-2.506841,-44.298528,80,26),
    (-23.589625,-46.673441,65,18)
]

@pytest.mark.parametrize("lat,lng,temperature,expected",test_array)
def test_get_temperature_by_lat_lng(lat,lng,temperature,expected):

    mock_get_patcher = patch('main.requests.get')

    temperature = {
        "currently":{
            "temperature": temperature
        }
    }

    mock_get = mock_get_patcher.start()

    mock_get.return_value.json.return_value = temperature

    response = get_temperature(lat, lng)

    mock_get.stop()

    assert response == expected