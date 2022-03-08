import pytest
from iaswrapper import get_apps

@pytest.fixture()
def appsec_keys():
    #response only for returning the test data
    return {'metadata', 'data', 'links '}



def test_api_info():
    """Tests and API to Insight AppSec to get configured Apps info"""

    response = app_instance.info()

    assert isinstance(response, dict)
